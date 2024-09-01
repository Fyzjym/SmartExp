import os
import random
from tqdm import tqdm
import string


def is_alpha_only(s: str) -> bool:

    valid_chars = set(string.ascii_letters)  # ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(valid_chars) == 0:
        return False

    for char in s:
        if char not in valid_chars:
            return False

    return True


def process_image_paths(input_path, output_txt_path, random_seed, save_number, num_to_save, mode='none'):
    # 获取所有图像路径和图像名

    image_paths_and_names = []
    for folder_name in os.listdir(input_path):
        folder_path = os.path.join(input_path, folder_name)


        if os.path.isdir(folder_path):

            folder_images = os.listdir(folder_path)
            for image_name in folder_images:
                image_path = os.path.join(folder_path, image_name)
                img_content = image_name.split('_')[-1].replace('.png', '')
                image_paths_and_names.append((image_path, img_content))

        else: # folder_path: no dir, is file

            image_path = folder_path
            # img_content = image_name.split('_')[-1].replace('.png', '')
            if mode == "vatr":
                img_content = image_path.split('_')[-1].replace('.png', '')
            if mode == "ddpm":
                img_content = image_path.split('__')[-1].replace('.png', '') # DDPM
            if mode == "gw":
                img_content = image_path.split('/')[-1].split('-')[1].split('.')[-1]
            if mode == 'CVL_dataset':
                img_content = image_path.split('-')[-1].replace('.png', '')
                if not is_alpha_only(img_content):
                    continue
            if mode == 'GWO_dataset':
                img_content = image_path.split('_')[-1].replace('.png', '')
                if not is_alpha_only(img_content):
                    continue
            image_paths_and_names.append((image_path, img_content))

    # 随机打乱图像路径和图像名
    random.seed(random_seed)
    random.shuffle(image_paths_and_names)

    # 选择前 num_to_save 对数据保存到文件中，同时显示进度条
    output_folder = f"save_{save_number}"
    os.makedirs(output_folder, exist_ok=True)
    output_txt_path = os.path.join(output_folder, output_txt_path)
    with open(output_txt_path, 'w') as f, tqdm(total=num_to_save, desc="Processing") as pbar:
        for i, (image_path, img_content) in enumerate(image_paths_and_names):
            if i >= num_to_save:
                break
            f.write(f"{image_path}\n{img_content}\n")
            pbar.update(1)

    print(f"save @ {output_txt_path}")

if __name__ == "__main__":
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr-main/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FL/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC1/saved_images/7000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC1_FL_2/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC1_FL_2/saved_images/7000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC_tau_a/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC_tau_a/saved_images/7000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC1/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC_tau_a_FL_2/saved_images/4000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20230709_VATr/VATr_FCC_tau_a_FL_2/saved_images/7000_model/HTR_boost"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240125_loacl_HTG/VATrVm-exp21_R_aff_scattention/saved_images_HTR_boost/9500_model"
    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240125_loacl_HTG/VATrVm-exp21_R_aff_scattention/saved_images_HTR_boost/15500_model"

    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/x_HTR_FAKE_data/05_VATR_raw"
    # input_path = "/home/WeiHongxi/Node95/Ym/data/cvl-database-1-1/trainset/words_gray_all"
    # input_path = "/home/WeiHongxi/Node95/Ym/data/cvl-database-1-1/testset/words_gray_all"

    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/x_HTR_FAKE_data/07_VATR_raw_CVL"

    # input_path = "/home/WeiHongxi/Node95/Ym/data/gw-online-dataset-master/GWO_tra"
    # input_path = "/home/WeiHongxi/Node95/Ym/data/gw-online-dataset-master/GWO_test"

    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/x_HTR_FAKE_data/08_VATR_raw_GWO"

    # input_path = "/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/x_HTR_FAKE_data/04_DDPM"

    input_path = "/home/WeiHongxi/Node95/Ym/Project_20240618_StyleGuided_HTG/exp05_StyleGuided_HTG_RAW_EXP_IMPORTANT/saved_images_HTR_boost/6500_model"

    # output_txt_name = "08_VATr_05_44419.lst"
    # output_txt_name = "10_VATr_025_35_4913_pick.lst"
    # output_txt_name = "12_CVL_dataset_test.lst"
    # output_txt_name = "13_VATr_CVL_05k.lst"
    # output_txt_name = "16_GWO_dataset_test.lst"
    # output_txt_name = "18_VATr_GWO_025k.lst"
    # output_txt_name = "19_VATr_CVL_1k.lst"
    # output_txt_name = "21_DDPM_IAM_05k.lst"

    output_txt_name = "23_ASNET_E6500_IAM_294780.lst"


    random_seed = 42  # 可以更改随机种子
    save_number = 44419  # 按照指定数字保存文件夹
    num_to_save = int(44419*1)  # 需要保存的数据对数

    # num_to_save = int(44419*0.5)  # 需要保存的数据对数
    # num_to_save = int(44419*0.25)  # 需要保存的数据对数
    # num_to_save = int(12147*1)  # 需要保存的数据对数
    # num_to_save = int(3624*0.5)  # 需要保存的数据对数
    # num_to_save = int(3624*1)  # 需要保存的数据对数


    process_image_paths(input_path, output_txt_name, random_seed, save_number, num_to_save, mode='vatr')

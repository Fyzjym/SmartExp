#python tool/create_dataset.py --out lmdb/data/iamTra20w --file /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_byHTR/crnn-pytorch-master/tra20.GANwriting.IAM

#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_new_byHTG/data/ym_GANwriting9420Gen_IAM/IAM_44000_1 --file /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_byHTR/A_GANwriting/ym_data_GT_gen/fake.img.60wid.44000_1.ym.GANwriting_9420
#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_new_byHTG/data/ym_GANwriting9420Gen_IAM/IAM_44000_2 --file /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_byHTR/A_GANwriting/ym_data_GT_gen/fake.img.60wid.44000_2.ym.GANwriting_9420
#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_new_byHTG/data/ym_GANwriting9420Gen_IAM/IAM_44000_3 --file /home/WeiHongxi/Node95/Ym/Project_HTR_Boost_byHTR/A_GANwriting/ym_data_GT_gen/fake.img.60wid.44000_3.ym.GANwriting_9420
#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/A_GANwriting_boostHTR/data/GANwriting_4000_FL_baseIAM/GANwritingFL_IAM_44000_1 --file /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/A_GANwriting_boostHTR/data_build/fake.img.60wid.44000_1.GANwriting_4000_FL
#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/B_VATr_boostHTR/data/VATrCE_IAM_44000_1 --file /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/B_VATr_boostHTR/data_build/save_44000/fake.img.60wid.44000_1.VATr_4000_CE
#python tool/create_dataset.py --out /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/B_VATr_boostHTR/data/VATrFL_IAM_44000_1 --file /home/WeiHongxi/Node95/Ym/Project_20230405_HTG_In_LongTail/B_VATr_boostHTR/data_build/save_44000/fake.img.60wid.44000_1.VATr_4000_FL


out_path="/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/x_HTR_FAKE_ASNET/02_ASNET_6500"
file_path="/home/WeiHongxi/Node95/Ym/Project_20240529_HTG_boost_HTR/z_data_build/save_44419/23_ASNET_E6500_IAM_294780.lst"
python tool/create_dataset.py --out "$out_path" --file "$file_path"
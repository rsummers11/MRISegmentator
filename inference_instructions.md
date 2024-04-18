#### **Instructions to run TS4MR-T1W on Biowulf cluster**


1. Setup a standalone virtual environment for TS4MR-T1W on the Biowulf cluster. Note that here I use `mamba` to manage virtual environments, which equals to `conda` if you use 'conda'
      
    <font size="2"> `mamba create -n nnUnetV2_test python=3.9` </font>

2. Install the latest nnUnetV2 from github 
   
   <font size="2"> `mamba activate nnUnetV2_test # First to activate the new environment` </font>  
   <font size="2"> `git clone https://github.com/MIC-DKFZ/nnUNet.git` </font>  
   <font size="2"> `cd nnUNet` </font>  
   <font size="2"> `pip install -e .` </font>  

3. Setting some environment variables, so that nnUnet can find where the trained models are.   

    <font size="2"> `export nnUNet_raw="/data/drdcad/yanzhuang3/segmentation-nnUnet-v2/nnUNet_raw/"`</font>    
    <font size="2"> `export nnUNet_preprocessed="/data/drdcad/yanzhuang3/segmentation-nnUnet-v2/nnUNet_preprocessed"`</font>    
    <font size="2"> `export nnUNet_results="/data/drdcad/yanzhuang3/segmentation-nnUnet-v2/nnUNet_results"`</font>  

4. Organizing the inference dataset like a tree structure:

        INPUT_FOLDER
        ├── t1w_subject_01_0000.nii.gz
        ├── t1w_subject_02_0000.nii.gz
        ├── t1w_subject_03_0000.nii.gz
        ├── t1w_subject_04_0000.nii.gz
        ├── t1w_subject_05_0000.nii.gz
        ├── t1w_subject_06_0000.nii.gz
        ├── ...     

    Please note that the filenames must start with a unique identifier, ***followed by a 4-digit modality identifier***. For more details see this: https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format_inference.md .    

5. Running inference using the command below: first for prediction, then for post-processing. Please note that you need to specify the paths of `INPUT_FOLDER`, `OUTPUT_FOLDER`, and `OUTPUT_FOLDER_PP` for input, output, outputs after post-processing. 

    <font size="2"> `nnUNetv2_predict -d Dataset885_IN_HOUSE_TS4MR_MR_ACTIVE_LEARNING_NEW_70_labels_2ND_ITER -i INPUT_FOLDER -o OUTPUT_FOLDER -f  0 1 2 3 4 -tr nnUNetTrainer -c 3d_fullres -p nnUNetPlans`</font>        
        
    <font size="2"> `nnUNetv2_apply_postprocessing -i OUTPUT_FOLDER -o OUTPUT_FOLDER_PP -pp_pkl_file /data/drdcad/yanzhuang3/segmentation-nnUnet-v2/nnUNet_results/Dataset885_IN_HOUSE_TS4MR_MR_ACTIVE_LEARNING_NEW_70_labels_2ND_ITER/nnUNetTrainer__nnUNetPlans__3d_fullres/crossval_results_folds_0_1_2_3_4/postprocessing.pkl -np 8 -plans_json /data/drdcad/yanzhuang3/segmentation-nnUnet-v2/nnUNet_results/Dataset885_IN_HOUSE_TS4MR_MR_ACTIVE_LEARNING_NEW_70_labels_2ND_ITER/nnUNetTrainer__nnUNetPlans__3d_fullres/crossval_results_folds_0_1_2_3_4/plans.json` </font>      

6. Once done, go to the results folder (e.g., `OUTPUT_FOLDER_PP`) to view the results. You can view the results using itk-snap and load label description file `final_mr_labels.txt`.    


#### **Instructions to run MRISegmentator**  


1. Setup a standalone virtual environment, called "nnUnetV2_test". Please note that here it uses `mamba` to manage virtual environments, which equals to `conda` if you use 'conda'
      
    <font size="2"> `mamba create -n nnUnetV2_test python=3.9` </font>

2. Install the latest nnUnetV2 from github 
   
   <font size="2"> `mamba activate nnUnetV2_test # First to activate the new environment` </font>  
   <font size="2"> `git clone https://github.com/MIC-DKFZ/nnUNet.git` </font>  
   <font size="2"> `cd nnUNet` </font>  
   <font size="2"> `pip install -e .` </font>  

3. Setting some environment variables, in here you only need to setup the results variable "nnUNet_results", please configure this environment variable to point to the provided model weights, so that the nnUnet can find where the trained model is. For example, the model weights were downloaed in a folder named "MRISegmentator", then configure nnUNet_results as:

    <font size="2"> `export nnUNet_results="PATH_TO_MRISegmentator/MRISegmentator/nnUNet_results"`</font>

   In the nnUNet_results folder, the folder structure should look like
        nnUNet_results
        ├── Dataset256_MRISeg
             ├── nnUNetTrainer__nnUNetPlans__3d_fullres
                      ├── fold_0

5. Organizing the inference dataset like a tree structure:

        INPUT_FOLDER
        ├── t1w_subject_01_0000.nii.gz
        ├── t1w_subject_02_0000.nii.gz
        ├── t1w_subject_03_0000.nii.gz
        ├── t1w_subject_04_0000.nii.gz
        ├── t1w_subject_05_0000.nii.gz
        ├── t1w_subject_06_0000.nii.gz
        ├── ...     

    Please note that the filenames must start with a unique identifier, ***followed by a 4-digit modality identifier***. For more details see this: https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/dataset_format_inference.md .    

6. Running inference using the command below. Please note that you need to specify the paths of `INPUT_FOLDER` and `OUTPUT_FOLDER` for input folder for the input and output folder for results. 

    <font size="2"> `nnUNetv2_predict -d Dataset256_MRISeg -i INPUT_FOLDER -o OUTPUT_FOLDER -f 0 -tr nnUNetTrainer -c 3d_fullres -p nnUNetPlans`</font>        

7. Once done, go to the results folder (e.g., `OUTPUT_FOLDER_PP`) to view the results. You can view the results using itk-snap and load label description file `final_mr_labels.txt`.    


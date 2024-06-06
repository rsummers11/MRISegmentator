<p align="center">
  <img src="assets/MRISegmentatorLogo.png?raw=true" width="40%" />
</p>

## **MRISegmentator-Abdomen**

**MRISegmentator-Abdomen: A Fully Automated Multi-Organ and Structure Segmentation Tool for T1-weighted Abdominal MRI**  

[Yan Zhuang](https://yanzhuang.me/)<sup>1</sup>, Tejas Sudharshan Mathai<sup>1, *</sup>, Pritam Mukherjee<sup>1, *</sup>, Brandon Khoury<sup>2</sup>, Boah Kim<sup>1</sup>,  Benjamin Hou<sup>1</sup>, Nusrat Rabbee<sup>3</sup>, and Ronald M. Summers<sup>1</sup>  
 
<sup>1</sup> Imaging Biomarkers and Computer-Aided Diagnosis Laboratory, NIH Clinical Center  
<sup>2</sup> Department of Radiology, Walter Reed National Military Medical Center   
<sup>3</sup> Biostatistics and Clinical Epidemiology Services, NIH Clinical Center   
<font size="2"><sup>*</sup> equal contribution </font> 

[[Paper](https://arxiv.org/abs/2405.05944)]   [[Dataset(coming soon!)](https://)]   

**Acknowledgement**: We would like to acknowledge [Abhinav Suri](https://abhinavsuri.com/) for his invaluable support to create the pip package. This work was supported by the Intramural Research Program of the National Institutes of Health (NIH) Clinical Center (project number 1Z01 CL040004). This work used the computational resources of the NIH HPC Biowulf cluster. We thank ChatGPT 4o for generating the logo used in this project.

<p align="center">
  <img src="assets/organ_structure_examples.png?raw=true" width="90%" />
</p>

## **Usage**

**Requirements**: We recommend running on a computer with a GPU. This package can be run on a computer with a CPU, but it will take a very long time to process a single scan.

**Step 1**: Create a virtual environment and install the package.  
We recommend you install MRISegmentator in a conda environment to avoid dependency conflicts. Note you can use any version of python that supports nnUNet v2.2 or above

```python 
conda create -n MRISegmentator python=3.11
conda activate MRISegmentator  
pip install MRISegmentator
```

**Step 2**: Run!

```sh
MRISegmentator -i path/to/input/mri.nii.gz -o path/to/output/segmentation.nii.gz -d gpu
```

*Notes*:   

* The model weights will download on their own to one of the following directories:
  - if the environment variable `MRISEGMENTATOR_DIR` is set, we will download to that directory (and create the directory if it does not exist)
  - if that environment variable is not set, it will download to the home directory at `~/.mrisegmentator_weights`.
  - You can also specify a directory for the weights via the `-m` option (this must be a path to the extracted folder from [this zip file](https://nihcc.app.box.com/index.php?rm=box_download_shared_file&shared_name=q6vl3015hteoufz7jll63u3hdqk79li7&file_id=f_1544045874167))

* For the `-d` option, you can also provide `cpu` or `mps` as an option (cpu runs on your computer's CPU only and mps runs on M1/2 processors).  

## Python API


You can also run this package via importing it in a python script:

```python
from mrisegmentator.inference import mri_segmentator
input_file_path = # path to your input file /mypath/input/input.nii.gz
output_file_path = # path to where you want to segmentation to save. e.g. /mypath/result/out.nii.gz
device = # one of 'gpu', 'cpu', 'mps'
path_to_model = # path to a trained nnunet model, if None will attempt to search for model weights above
mri_segmentator(input_file_path, output_file_path, path_to_model, device)
```

### Redownloading weights

Normally, we handle downloading the weights for you, but if we release a new model version, we will need you to redownload the weights via the following command

```
MRISegmentator_Redownload
```

The last time model weights were changed was on **May 30, 2024**.


### Issues
MRISegmentator is a research-grade segmentation tool currently under active development. Please let us know if you encounter any issues or have suggestions for improvements.

### References
If you find our work is useful for your research, please cite
```bib
@article{zhuang2024mrisegmentator,
  title={MRISegmentator-Abdomen: A Fully Automated Multi-Organ and Structure Segmentation Tool for T1-weighted Abdominal MRI},
  author={Zhuang, Yan and Mathai, Tejas Sudharshan and Mukherjee, Pritam and Khoury, Brandon and Kim, Boah and Hou, Benjamin and Rabbee, Nusrat and Summers, Ronald M},
  journal={arXiv preprint arXiv:2405.05944},
  year={2024}
}
```

We used nnUnet in our research, please also consider citing  

```bib
@article{isensee2021nnu,
  title={nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation},
  author={Isensee, Fabian and Jaeger, Paul F and Kohl, Simon AA and Petersen, Jens and Maier-Hein, Klaus H},
  journal={Nature methods},
  volume={18},
  number={2},
  pages={203--211},
  year={2021},
  publisher={Nature Publishing Group}
}
```

### Segmentation labels

Below is a table that maps the segmentation codes to the original bodypart name, or   

[Here](resources/MRISegmentator_ITK_LabelMap.txt) you can find the itk-snap label description.

|Organ or Structure name | Label|
|:-----|:-----|
spleen |1 | 
kidney_right | 2 | 
kidney_left | 3 | 
gallbladder | 4 | 
liver | 5 | 
esophagus | 6 |  
stomach | 7 | 
aorta	| 8 |
inferior_vena_cava | 9 |
portal_vein_and_splenic_vein |	10 |
pancreas |	11 |
adrenal_gland_right |	12 |
adrenal_gland_left |	13 |
lung_right |	14 |
lung_left |	15 |
small_bowel |	16 |
duodenum |	17 |
colon |	18 |
iliac_artery_left |	19 |
iliac_artery_right |	20 |
iliac_vena_left |	21 |
iliac_vena_right |	22 |
gluteus_maximus_left |	23 |
gluteus_maximus_right |	24 |
gluteus_medius_left |	25 |
gluteus_medius_right |	26 |
autochthon_left |	27 |
autochthon_right |	28 |
iliopsoas_left |	29 |
iliopsoas_right |	30 |
hip_left |	31 |
hip_right |	32 |
sacrum |	33 |
rib_left_4 |	34 |
rib_left_5 |	35 |
rib_left_6 |	36 |
rib_left_7 |	37 |
rib_left_8 |	38 |
rib_left_9 |	39 |
rib_left_10 |	40 |
rib_left_11 |	41 |
rib_left_12 |	42 |
rib_right_4 |	43 |
rib_right_5 |	44 |
rib_right_6 |	45 |
rib_right_7 |	46 |
rib_right_8 |	47 |
rib_right_9 |	48 |
rib_right_10 |	49 |
rib_right_11 |	50 |
rib_right_12 |	51 |
vertebrae_L5 |	52 |
vertebrae_L4 |	53 |
vertebrae_L3 |	54 |
vertebrae_L2 |	55 |
vertebrae_L1 |	56 |
vertebrae_T12 |	57 |
vertebrae_T11 |	58 |
vertebrae_T10 |	59 |
vertebrae_T9 |	60 |
vertebrae_T8 |	61 |
vertebrae_T7 |	62 |


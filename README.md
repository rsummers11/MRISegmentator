<p align="center">
  <img src="assets/MRISegmentatorLogo.png?raw=true" width="40%" />
</p>

## **MRISegmentator-Abdomen**

MRISegmentator-Abdomen: A Fully Automated Multi-Organ and Structure Segmentation Tool for T1-weighted Abdominal MRI  

[Yan Zhuang](https://yanzhuang.me/)$`1`$ , Tejas Sudharshan Mathai$`1,^*`$, Pritam Mukherjee$`1,^*`$, Brandon Khoury$`2`$, Boah Kim$`1`$,  Benjamin Hou$`1`$, Nusrat Rabbee$`3`$, and Ronald M. Summers$`1`$  
 
$`1`$ Imaging Biomarkers and Computer-Aided Diagnosis Laboratory, NIH Clinical Center  
$`2`$ Department of Radiology, Walter Reed National Military Medical Center   
$`3`$ Biostatistics and Clinical Epidemiology Services, NIH Clinical Center   
<font size="2"> $`^*`$ equal contribution </font> 

**Acknowledgement**: We would like to acknowledge [Abhinav Suri](https://abhinavsuri.com/) for his invaluable support to create the pip package. This work was supported by the Intramural Research Program of the National Institutes of Health (NIH) Clinical Center (project number 1Z01 CL040004). This work used the computational resources of the NIH HPC Biowulf cluster.

[Paper](https://arxiv.org/abs/2405.05944)   
[Dataset(coming soon!)](https://) 

---  

**Requirements**: We recommend running on a computer with a GPU. This package can be run on a computer with a CPU, but it will take a very long time to process a single scan.

**Step 1**: Create a virtual environment and install the package
We recommend you install MRISegmentator in a conda environment to avoid dependency conflicts. Note you can use any version of python that supports nnUNet v2.2 or above

```python 
conda create -n MRISegmentator python=3.11
conda activate
pip install MRISegmentator
```

**Step 2**: Download weights
Please use this link to download the model weights (Coming soon!)

**Step 3**: Run!

```python
MRISegmentator -i path/to/input/mri.nii.gz -o path/to/output/segmentation.nii.gz -d gpu -m path/to/model
```

For the -d option, you can also provide cpu or mps as an option (cpu runs on your computer's CPU only and mps runs on M1/2 processors).

You can also run this package via importing it in a python script:

```python
from mrisegmentator.inference import mri_segmentator
input_file_path = # path to your input file /mypath/input/input.nii.gz
output_file_path = # path to where you want to segmentation to save. e.g. /mypath/result/out.nii.gz
device = # one of 'gpu', 'cpu', 'mps'
path_to_model = # path to a trained nnunet mode
mri_segmentator(input_file_path, output_file_path, device, path_to_model)
```
### Segmentation labels

Below is a table that maps the segmentation codes to the original bodypart name

TA2 is a standardized way to name anatomy. Mostly the TotalSegmentator names follow this standard.
For some classes they differ which you can see in the table below.

[Here](resources/totalsegmentator_snomed_mapping.csv) you can find a mapping of the TotalSegmentator classes to SNOMED-CT codes.

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

### Issues
MRISegmentator is a research-grade segmentation tool currently under active development. Please let us know if you encounter any issues or have suggestions for improvements

### References
If you find our work is useful for your research, please consider citing
```bib
@article{zhuang2024mrisegmentator,
  title={MRISegmentator-Abdomen: A Fully Automated Multi-Organ and Structure Segmentation Tool for T1-weighted Abdominal MRI},
  author={Zhuang, Yan and Mathai, Tejas Sudharshan and Mukherjee, Pritam and Khoury, Brandon and Kim, Boah and Hou, Benjamin and Rabbee, Nusrat and Summers, Ronald M},
  journal={arXiv preprint arXiv:2405.05944},
  year={2024}
}
```

### MIT License (??? what license should we use?)
```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

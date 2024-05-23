<p align="center">
  <img src="assets/MRISegmentatorLogo.png?raw=true" width="40%" />
</p>

## **MRISegmentator-Abdomen**

**Imaging Biomarkers and Computer-Aided Diagnosis Laboratory, NIH Clinical Center**

Yan Zhuang, Tejas Sudharshan Mathai$`^*`$, Pritam Mukherjee$`^*`$, Brandon Khoury, Boah Kim,  Benjamin Hou, Nusrat Rabbee, and Ronald M. Summers  
<font size="2"> $`^*`$ equal contribution </font>

**Acknowledgement**: We would like to acknowledge [Abhinav Suri](https://abhinavsuri.com/) for his invaluable support to create the pip package. This work was supported by the Intramural Research Program of the National Institutes of Health (NIH) Clinical Center (project number 1Z01 CL040004). This work used the computational resources of the NIH HPC Biowulf cluster.

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

|Index|Organ or Structure name|
|:-----|:-----|
1 | spleen ||
2 | kidney_right ||
3 | kidney_left ||
4 | gallbladder ||
5 | liver ||
6 | stomach ||
7 | pancreas ||
8 | adrenal_gland_right | suprarenal gland |
9 | adrenal_gland_left | suprarenal gland |
10 | lung_upper_lobe_left | superior lobe of left lung |
11 | lung_lower_lobe_left | inferior lobe of left lung |
12 | lung_upper_lobe_right | superior lobe of right lung |
13 | lung_middle_lobe_right | middle lobe of right lung |
14 | lung_lower_lobe_right | inferior lobe of right lung |
15 | esophagus ||
16 | trachea ||
17 | thyroid_gland ||
18 | small_bowel | small intestine |
19 | duodenum ||
20 | colon ||
21 | urinary_bladder ||
22 | prostate ||
23 | kidney_cyst_left ||
24 | kidney_cyst_right ||
25 | sacrum ||
26 | vertebrae_S1 ||
27 | vertebrae_L5 ||
28 | vertebrae_L4 ||
29 | vertebrae_L3 ||
30 | vertebrae_L2 ||
31 | vertebrae_L1 ||
32 | vertebrae_T12 ||
33 | vertebrae_T11 ||
34 | vertebrae_T10 ||
35 | vertebrae_T9 ||
36 | vertebrae_T8 ||
37 | vertebrae_T7 ||
38 | vertebrae_T6 ||
39 | vertebrae_T5 ||
40 | vertebrae_T4 ||
41 | vertebrae_T3 ||
42 | vertebrae_T2 ||
43 | vertebrae_T1 ||
44 | vertebrae_C7 ||
45 | vertebrae_C6 ||
46 | vertebrae_C5 ||
47 | vertebrae_C4 ||
48 | vertebrae_C3 ||
49 | vertebrae_C2 ||
50 | vertebrae_C1 ||
51 | heart ||
52 | aorta ||
53 | pulmonary_vein ||
54 | brachiocephalic_trunk ||
55 | subclavian_artery_right ||
56 | subclavian_artery_left ||
57 | common_carotid_artery_right ||
58 | common_carotid_artery_left ||
59 | brachiocephalic_vein_left ||suprarenal gland
60 | brachiocephalic_vein_right ||
61 | atrial_appendage_left ||
62 | superior_vena_cava ||
63 | inferior_vena_cava ||
64 | portal_vein_and_splenic_vein | hepatic portal vein |
65 | iliac_artery_left | common iliac artery |
66 | iliac_artery_right | common iliac artery |
67 | iliac_vena_left | common iliac vein |
68 | iliac_vena_right | common iliac vein |
69 | humerus_left ||
70 | humerus_right ||
71 | scapula_left ||
72 | scapula_right ||
73 | clavicula_left | clavicle |
74 | clavicula_right | clavicle |
75 | femur_left ||
76 | femur_right ||
77 | hip_left ||
78 | hip_right ||
79 | spinal_cord ||
80 | gluteus_maximus_left | gluteus maximus muscle |
81 | gluteus_maximus_right | gluteus maximus muscle |
82 | gluteus_medius_left | gluteus medius muscle |
83 | gluteus_medius_right | gluteus medius muscle |
84 | gluteus_minimus_left | gluteus minimus muscle |
85 | gluteus_minimus_right | gluteus minimus muscle |
86 | autochthon_left ||
87 | autochthon_right ||
88 | iliopsoas_left | iliopsoas muscle |
89 | iliopsoas_right | iliopsoas muscle |
90 | brain ||
91 | skull ||
92 | rib_left_1 ||
93 | rib_left_2 ||
94 | rib_left_3 ||
95 | rib_left_4 ||
96 | rib_left_5 ||
97 | rib_left_6 ||
98 | rib_left_7 ||
99 | rib_left_8 ||
100 | rib_left_9 ||
101 | rib_left_10 ||
102 | rib_left_11 ||
103 | rib_left_12 ||
104 | rib_right_1 ||
105 | rib_right_2 ||
106 | rib_right_3 ||
107 | rib_right_4 ||
108 | rib_right_5 ||
109 | rib_right_6 ||
110 | rib_right_7 ||
111 | rib_right_8 ||
112 | rib_right_9 ||
113 | rib_right_10 ||
114 | rib_right_11 ||
115 | rib_right_12 ||
116 | sternum ||
117 | costal_cartilages ||

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

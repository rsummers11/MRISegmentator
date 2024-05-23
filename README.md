### **MRISegmentator-Abdomen**

<p float="left">
  <img src="assets/MRISegmentatorLogo.png?raw=true" width="37.25%" />
</p>

**Imaging Biomarkers and Computer-Aided Diagnosis Laboratory, NIH Clinical Center**

Yan Zhuang, Tejas Sudharshan Mathai$`^*`$, Pritam Mukherjee$`^*`$, Brandon Khoury, Boah Kim,  Benjamin Hou, Nusrat Rabbee, Ronald M. Summers  
($`^*`$ equal contribution)

Acknowledgement: 

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

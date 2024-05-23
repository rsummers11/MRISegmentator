#### **MRISegmentator-Abdomen**

Requirements: We recommend running on a computer with a GPU. This package can be run on a computer with a CPU, but it will take a very long time to process a single scan.

Step 1: Create a virtual environment and install the package
We recommend you install MRISegmentator in a conda environment to avoid dependency conflicts. Note you can use any version of python that supports nnUNet v2.2 or above

<font size="2"> `conda create -n MRISegmentator python=3.11` </font>
<font size="2"> `conda activate` </font>
<font size="2"> `pip install MRISegmentator` </font>

Step 2: Download weights
Please use this link to download the model weights (Coming soon!)

Step 3: Run!

<font size="2"> `MRISegmentator -i path/to/input/mri.nii.gz -o path/to/output/segmentation.nii.gz -d gpu -m path/to/model` </font>

For the -d option, you can also provide cpu or mps as an option (cpu runs on your computer's CPU only and mps runs on M1/2 processors).

You can also run this package via importing it in a python script:

from mrisegmentator.inference import mri_segmentator

```python
input_file_path = # path to your input file /mypath/input/input.nii.gz
output_file_path = # path to where you want to segmentation to save. e.g. /mypath/result/out.nii.gz
device = # one of 'gpu', 'cpu', 'mps'
path_to_model = # path to a trained nnunet mode
mri_segmentator(input_file_path, output_file_path, device, path_to_model)
```

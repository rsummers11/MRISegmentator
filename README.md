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

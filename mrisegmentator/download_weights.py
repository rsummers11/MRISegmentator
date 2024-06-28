"""
function: automatically downloading model weights for the MRISegmentator package
author = "Abhinav Suri, Yan Zhuang"
license = "Please see the license file"
email = "yan.zhuang2@nih.gov or rsummers@mail.cc.nih.gov"
Date: 06/27/2024
"""

import requests
from tqdm import tqdm
import os
from pathlib import Path
import zipfile

def get_weights_dir():
    """
    Create directory to store model weights
    """
    env_var = 'MRISEGMENTATOR_DIR'
    if os.environ.get('MRISEGMENTATOR_DIR') is not None:
        dir = os.environ.get('MRISEGMENTATOR_DIR')
    else:
        dir = str(Path.home()) + '/.mrisegmentator_weights'
    try:
        if not os.path.isdir(dir):
            print("making mrisegmentator directory at:", dir)
            os.makedirs(dir)
        return dir
    except Exception as e:
        raise FileNotFoundError(f"cannot create directory to store weights at {dir}: ERROR: {e}")

def download_weights(redownload=False):
    """
    download the weights automatically
    """
    url = 'https://nihcc.app.box.com/index.php?rm=box_download_shared_file&shared_name=q6vl3015hteoufz7jll63u3hdqk79li7&file_id=f_1544045874167'
    
    filepath = get_weights_dir() + '/MRISegmentator.zip'
    final_path = get_weights_dir() + '/nnUNetTrainer__nnUNetPlans__3d_fullres_New'
    if os.path.exists(final_path) and redownload == False:
        print("Weights are already downloaded at", final_path)
        return final_path
    if not os.path.exists(final_path) or redownload == True:
        print("saving weights to", get_weights_dir())
        # from https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests 
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(filepath, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError('Could not download weights')
    if os.path.exists(filepath):
        print("unzipping model weights")
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(get_weights_dir())
            if os.path.exists(final_path):
                print("successfully unzipped weights and saved to", final_path, ". Cleaning up...")
                os.remove(filepath)
                return final_path
    else:
        raise FileNotFoundError(f"for some reason the MRISegmentator.zip file was not found in your weights directory at: {get_weights_dir()}")

def force_redownload():
    download_weights(True) 

if __name__ == "__main__":
    download_weights()

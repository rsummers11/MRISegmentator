"""
function: inference script for the MRISegmentator package
author = "Abhinav Suri, Yan Zhuang"
license = "Please see the license file"
email = "yan.zhuang2@nih.gov or rsummers@mail.cc.nih.gov"
Date: 06/27/2024
"""

from batchgenerators.utilities.file_and_folder_operations import join
import os
import contextlib
import sys
import warnings
from .download_weights import download_weights

class DummyFile:
    def write(self, x): pass
    def flush(self): pass

@contextlib.contextmanager
def nostdout(verbose=False):
    if not verbose:
        save_stdout = sys.stdout
        sys.stdout = DummyFile()
        yield
        sys.stdout = save_stdout
    else:
        yield


def mri_segmentator(input_file, output_file, path_to_model, device='gpu'):

    print("Checking inputs")
    if input_file.find('.nii') == -1:
        raise ValueError("invalid file type: must have .nii in filename")
    if os.path.exists(input_file) == False:
        raise ValueError("path to input file must exist")
    if device not in ['gpu', 'cpu', 'mps']:
        raise ValueError("invalid device: must be one of 'gpu', 'cpu', or 'mps'")

    # nnunet needs absolute path to a file to handle cases where user supplies bare filename

    output_file = os.path.abspath(output_file)

    if path_to_model is None:
        path_to_model = download_weights()

    if not os.path.isdir(path_to_model):
        raise ValueError("invalid path to trained model folder")

    print("setup devices") 

    import torch

    if device == 'gpu':
        devicet = torch.device('cuda')
    elif device == 'cpu':
        devicet = torch.device('cpu')
    elif device == 'mps':
        devicet = torch.device('mps')

    if device == 'cpu':
        import multiprocessing
        torch.set_num_threads(multiprocessing.cpu_count())

    os.environ['nnUNet_raw'] = output_file
    os.environ['nnUNet_preprocessed'] = output_file
    os.environ['nnUNet_results'] = output_file
    # os.environ['nnUNet_preprocessed'] = str(path_to_model)
    # os.environ['nnUNet_results'] = str(path_to_model)

    warnings.filterwarnings("ignore", category=UserWarning, module="nnunetv2")
    with nostdout():
        from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor

    print("Instantiating nnunet predictor...")
    with nostdout():
        predictor = nnUNetPredictor(
            tile_step_size=0.5,
            use_gaussian=True,
            use_mirroring=False,
            perform_everything_on_device=True,
            device=devicet,
            verbose=False,
            verbose_preprocessing=False,
            allow_tqdm=True
        )

   
    print("Instantiating trained model...")
    with nostdout():
        predictor.initialize_from_trained_model_folder(
            path_to_model,
            use_folds=(0,1,2,3,4) if device != 'cpu' else (0,),
            checkpoint_name='checkpoint_final.pth',
        )

    print("Starting prediction...")
    with nostdout():
        predictor.predict_from_files([[input_file]],
             [output_file],
             save_probabilities=False, overwrite=True,
             num_processes_preprocessing=1, num_processes_segmentation_export=1,
             folder_with_segs_from_prev_stage=None, num_parts=1, part_id=0)
    print("Cleaning up...")
    for i in ['dataset.json', 'plans.json', 'predict_from_raw_data_args.json']:
        try:
            os.remove(os.path.dirname(os.path.abspath(output_file)) + '/' + i)
        except Exception as e:
            print(i, e)
            pass
    print("DONE!")

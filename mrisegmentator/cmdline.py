import argparse


def main():
    parser = argparse.ArgumentParser(description="Segment 68 anatomical structures on T1 weighted MRI. Model by Yan Zhuang. Package by Abhinav Suri. If you use this tool cite https://arxiv.org/abs/2405.05944")

    parser.add_argument("-i", metavar="filepath", dest="input",
                        help="Path to MR nifti image", required=True)

    parser.add_argument("-o", metavar="filepath", dest="output",
                        help="Output filepath for segmentation masks",
                        required=False)
    
    parser.add_argument("-d", "--device", choices=["gpu", "cpu", "mps"],
                        help="Device to run on (default: gpu).",
                        default="gpu")
    
    parser.add_argument("-m", metavar="directory", dest="path_to_model",
                        help="Path to trained nnunet model",
                        required=True)

    args = parser.parse_args()

    from .inference import mri_segmentator

    mri_segmentator(args.input, args.output, args.device, args.path_to_model)

if __name__ == "__main__":
    main()

from vidstab.VidStab import VidStab
import ffmpeg
import os
import argparse


#note: need to do avi -> mp4 cropped -> (avi stabbed) -> avi compped

def arg_parse():
    """
    Parse arguements to the detect module

    """


    parser = argparse.ArgumentParser(description='Crops and Stabilizes Videos')

    parser.add_argument("--video", dest = 'video', help =
                        "Video to crop and stabilize",
                        default = "MOVI009.AVI", type = str)
    parser.add_argument("--outcrop", dest = 'cropvid_name', help =
                        "Name of the output cropped file", default = "cropped.mp4",
                        type = str)
    parser.add_argument("--outstab", dest = 'stabvid_name', help=
                        "Name of the output stabilized file", default = "stabbed.avi",
                        type = str)
    return parser.parse_args()

args = arg_parse()

cropped = args.cropvid_name
stable = args.stabvid_name

(
    ffmpeg
    .input(filename=args.video)
    .crop(0,689,1280,689)
    .output(filename=cropped)
    .run()
)


# Stabilize
stabilizer = VidStab()
stabilizer.stabilize(input_path=cropped, output_path=stable)

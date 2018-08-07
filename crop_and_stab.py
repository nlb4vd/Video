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
                        "Name of the output cropped file", default = "cropped2.mp4",
                        type = str)
    parser.add_argument("--outstab", dest = 'stabvid_name', help=
                        "Name of the output stabilized file", default = "stabbed2.avi",
                        type = str)
    return parser.parse_args()

def crop(video, cropvid_name):
    (
        ffmpeg
        .input(filename=video)
        .crop(0,689,1280,689)
        .output(filename=cropvid_name)
        .run()
    )

def stab(cropvid_name, stabvid_name):
    stabilizer = VidStab()
    stabilizer.stabilize(input_path=cropvid_name, output_path=stabvid_name)

if __name__=="__main__":
    args = arg_parse()
    crop(args.video, args.cropvid_name)
    stab(args.cropvid_name, args.stabvid_name)

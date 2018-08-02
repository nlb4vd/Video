import argparse
import ffmpeg

def arg_parse():
    """
    Parse arguements to the detect module

    """


    parser = argparse.ArgumentParser(description='Crops and Stabilizes Videos')

    parser.add_argument("--video", dest = 'video', help =
                        "Video to compress",
                        default = "video.avi", type = str)
    parser.add_argument("--outvid", dest = 'outvid_name', help =
                        "Name of the output compressed video", default = "compressed.avi",
                        type = str)
    return parser.parse_args()

args = arg_parse()

(
    ffmpeg
    .input(args.video)
    .output(args.outvid_name, crf=35 , vcodec='h264')
    .run()
)

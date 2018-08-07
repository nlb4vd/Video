#Currently only works if the input and output folder are in the current directory
#and the input and output are the names without a slash

import glob
import os
import argparse
import crop_and_stab as cas
import compress as com

def arg_parse():
    """
    Parse arguements to the detect module

    """

    parser = argparse.ArgumentParser(description='Takes in a directory of videos and outputs a second directory with a cropped and (optionally) stabilized version of each video')

    parser.add_argument("--input", dest = 'in_folder', help =
                        "Name of the folder containing movies (should be in the current directory and inputted without a '/' at the beginning)",
                        type = str)
    parser.add_argument("--output", dest = 'out_folder', help =
                        "Name of the output folder (should be in the current directory and inputted without a '/' at the beginning). Default is outFolder",
                        default = "processed", type = str)
    parser.add_argument("--stab", dest = 'stab_or_no', help=
                        "Whether or not to stabilize. Options are True or False, default is True",
                        default = "True", type = str)
    parser.add_argument("--deleteInter", dest= 'deleteInter', help=
                        "Whether or not to delete intermediate files. Options are True or False, default is True",
                        default = "True", type = str)
    return parser.parse_args()

args = arg_parse()

in_folder=args.in_folder
out_folder=args.out_folder
stab_or_no=args.stab_or_no=="True"
deleteInter=args.deleteInter=="True"

root = os.getcwd()
os.chdir(root+"/"+in_folder)

vids=[]

for file in glob.glob("*.avi"):
    #print(file)
    vids.append(file)

directory=root+"/"+out_folder
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir("..")

for file in vids:
    file_name=file[:-4]
    file=in_folder+"/"+file
    cropped_file=out_folder+"/"+file_name+"_cropped.mp4"
    cas.crop(file, cropped_file)
    if stab_or_no==True:
        stabbed_file=out_folder+"/"+file_name+"_stabbed.avi"
        cas.stab(cropped_file, stabbed_file)
        stabbed_comp_file=out_folder+"/"+file_name+"_stabbed_comp.avi"
        com.compress(stabbed_file, stabbed_comp_file)
    cropped_comp_file=out_folder+"/"+file_name+"_cropped_comp.avi"
    com.compress(cropped_file, cropped_comp_file)
    if deleteInter==True:
        os.remove(cropped_file)
        if stab_or_no==True:
            os.remove(stabbed_file)

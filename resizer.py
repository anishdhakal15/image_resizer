from cv2 import resize as imresize, IMREAD_UNCHANGED, INTER_AREA, imwrite, imread
from os import listdir
from os.path import isfile, join as pjoin, abspath, split as fsplit
from sys import argv


# source_path = "/home/anish/Documents/experiments/image_resizer/images"
# dest_path = "/home/anish/Documents/experiments/image_resizer/output"
# dimension = (750,480)
def resize(file_path,dest_path,dim):
    img = imread(file_path, IMREAD_UNCHANGED)
    resized = imresize(img, dim, interpolation = INTER_AREA)
    dest=abspath(pjoin(dest_path,str(dim[0])+'X'+str(dim[1])+'('+fsplit(file_path)[1]+')'))
    print(f'resizeing {file_path} to {dest}')
    imwrite(dest,resized)
def source_check():
    pass
def dest_check():
    pass
try:
    source_path = argv[1]
    dest_path = argv[2]
    if argv[3].isdigit() and argv[4].isdigit():
        width = int(argv[3])
        height = int(argv[4])
    else:
        raise Exception(f"only numbers are accepted as image resolution,{argv[3]} and {argv[4]} are given")
    dimension = (width,height)
except Exception as e:
    print(e)
    exit()


onlyfiles = [abspath(pjoin(source_path, f)) for f in listdir(source_path) if isfile(pjoin(source_path, f))]
[resize(i,dest_path,dimension) for i in onlyfiles]


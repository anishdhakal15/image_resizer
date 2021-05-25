from cv2 import resize as imresize, IMREAD_UNCHANGED, INTER_AREA, imwrite, imread
from os import listdir,mkdir
from os.path import isfile, join as pjoin, abspath, split as fsplit, isdir
from sys import argv

def resize(file_path,dest_path,dim):
    try:
        img = imread(file_path, IMREAD_UNCHANGED)
        resized = imresize(img, dim, interpolation = INTER_AREA)
        dest=abspath(pjoin(dest_path,str(dim[0])+'X'+str(dim[1])+'('+fsplit(file_path)[1]+')'))
        print(f'resizeing {file_path} to {dest}')
        imwrite(dest,resized)
    except:
        print(f"Error occur in file {file_path}")
def source_check(source_path):
    source = abspath(source_path)
    if isdir(source):
        files = [f for f in listdir(source_path) if isfile(pjoin(source_path, f))]
        print(files)
        if not files:
            raise Exception("empty directory")
    else:
        raise Exception("source directory not available")


def dest_check(dest_path):
    dest = abspath(dest_path)
    if not isdir(dest):
        print("Destination directory is not available, Do you want to create (y,n)")
        cho = input("Choice: ")
        if cho == 'y' or cho == 'Y':
            mkdir(dest)
        else:
            exit()
if argv[1]=='help':
    print("syntax \n python3 resizer.py source_address destination_address width height\n width and height must be integer")
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

source_check(source_path)
dest_check(dest_path)
onlyfiles = [abspath(pjoin(source_path, f)) for f in listdir(source_path) if isfile(pjoin(source_path, f))]
[resize(i,dest_path,dimension) for i in onlyfiles]


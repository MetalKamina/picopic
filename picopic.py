import numpy as np
import sys
import os
from PIL import Image

#4 sizes that fit in the pico-8 sprite section
#note: images are cropped to square because I didn't feel like preserving the aspect ratio
sizes = [
    (8,8),
    (16,16),
    (24,24),
    (32,32)
]

#colors from pico-8 wiki
colors = [
    [0, 0, 0],
    [29, 43, 83],
    [126, 37, 83],
    [0, 135, 81],
    [171, 82, 54],
    [95, 87, 79],
    [194, 195, 199],
    [255, 241, 232],
    [255, 0, 77],
    [255, 163, 0],
    [255, 236, 39],
    [0, 228, 54],
    [41, 173, 255],
    [131, 118, 156],
    [255, 119, 168],
    [255, 204, 170],
]

def pixel_comp(pixel):
    r,g,b = pixel
    dist = 1000
    ind = -1

    for i in range(len(colors)):
        cr,cg,cb = colors[i]

        #compares each pixel with euclidean (L2) distance
        tmp_dist = np.sqrt((r-cr)**2+(g-cg)**2+(b-cb)**2)
        if(tmp_dist < dist):
            dist = tmp_dist
            ind = i
    return ind

#parse args and make sure input is valid
def check_args(args):
    in_file,size,offx,offy,out = args[1:]
    size = int(size)
    offx = int(offx)
    offy = int(offy)
    endx = sizes[int(size)][0]+offx*8
    endy = sizes[int(size)][0]+offy*8
    if(not os.path.isfile(in_file)):
        print("Input file does not exist")
        exit()
    if(size < 0 or size > 3):
        print("Invalid size (must be in range [0,3])")
        exit()
    if(endx > 128):
        print("Invalid x offset (rightmost pixel position must not exceed 128)")
        exit()
    if(endy > 32):
        print("Invalid y offset (bottommost pixel position must not exceed 32)")
        exit()
    


def print_usage():
    print("python picopic.py \"path/to/file\" size offset_x offset_y \"path/to/output\"")

if __name__ == "__main__":
    if(len(sys.argv) != 6):
        print_usage()
        exit()
    args = sys.argv
    check_args(args)

    #open and convert image to usable format
    im = Image.open(args[1])
    im = im.convert("RGB")
    w,h = im.size

    #center crop images
    if(h < w):
        l = int((w-h)/2)
        r = w-l
        im = im.crop((l,0,r,h))
    else:
        t = int((h-w)/2)
        b = h-t
        im = im.crop((0,t,w,b))

    #resize images to argument specification
    im = im.resize(sizes[int(args[2])],resample=1)
    new_arr = np.zeros((32,64*4),dtype=int)
    im_arr = np.asarray(im)

    #final sizes of image
    w,h = sizes[int(args[2])]

    #calculate offset sizes
    offx = int(args[3])*8
    offy = int(args[4])*8

    #populate new array of pico-8 values
    for i in range(h):
        for j in range(w):
            new_arr[i+offy,j+offx] = pixel_comp(im_arr[i,j])

    #actual size of printable array
    printh = new_arr.shape[0]
    printw = new_arr.shape[1]
    with open(args[5],mode="w") as out_file:
        #pico-8 file header
        out_file.write("pico-8 cartridge // http://www.pico-8.com\nversion 36\n__gfx__\n")

        for i in range(printh):
            for j in range(printw):
                #convert decimal value to hex and write to file
                out_file.write(str(hex(new_arr[i,j]))[2:])
            out_file.write("\n")
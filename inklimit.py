from PIL import Image
import numpy as np
import sys

def inklimit():
    
    # read in system arguments 
    inklimit = int(sys.argv[3])
    out_name = sys.argv[2]
    in_name = sys.argv[1]

    # open in_name file 
    img = Image.open(in_name, 'r')
    arr = np.asarray(img)

    # inklimiting scale factor
    scale_img = inklimit/400
    arr_copy = np.copy(arr)
    scaled_arr = np.multiply(scale_img, arr_copy)

    # cast array as uint8 
    scaled_arr_cast = scaled_arr.astype('uint8')

    # save images to out_name path
    scaled_img = Image.fromarray(scaled_arr_cast, mode = 'CMYK')
    scaled_img.save(out_name, compression = 'tiff_deflate')

    return

inklimit()
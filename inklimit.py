def inklimit(inklimit = 400):
    from PIL import Image
    import numpy as np

    # path ends with ".tiff"
    path = '/Users/di/Dropbox/Code/GitHub/pairprogramming/testimage.tiff'
    img = Image.open(path, 'r')
    arr = np.asarray(img)

    print('arr.shape')

    chlimit = inklimit/4
    # map 0-255 onto 0-chlimit using numpy operation
    print(arr[0,0,0])
    return

inklimit()
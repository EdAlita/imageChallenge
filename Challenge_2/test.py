import cv2
import numpy as np
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import skimage, os
from skimage.morphology import ball, disk, dilation, binary_erosion, remove_small_objects, erosion, closing, reconstruction, binary_closing
from skimage.measure import label,regionprops, perimeter
from skimage.morphology import binary_dilation, binary_opening
from skimage.filters import roberts, sobel
from skimage import measure, feature
from skimage.segmentation import clear_border, mark_boundaries
from skimage import data
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.misc
from glob import glob
from skimage.io import imread, imsave
from skimage import img_as_ubyte

BASE_IMG_PATH=os.path.join('..','input')

def challenge_2(raw_im):
    im = raw_im.copy()
    binary = im < -200
    cleared = clear_boarder(binary)
    label_image = label(cleared, background=-1)
    areas = [r.area for r in regionprops(label_image)]
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area > np.median(areas):
                for coordinates in region.coords:                
                       label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image == 0
    selem = disk(5)
    binary = binary_erosion(binary, selem)
    selem = disk(2)
    binary = binary_closing(binary, selem, return_edges=True)
    edges = canny(binary)
    binary = ndi.binary_fill_holes(edges, structure=np.ones((5,5)))
    get_high_vals = binary != 0
    im[get_high_vals] = 255
    return im


test_image = imread("/home/edalita/Documents/MAIA/3-Semestre/eHealth/Challenge/q3.tif")
# Example usage
segmented_image = challenge_2(test_image)
segmented_image_ubyte = img_as_ubyte(segmented_image)  # Convert to 8-bit unsigned byte format
imsave('q1.png',segmented_image_ubyte)



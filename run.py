import spectral.io.envi as envi
import matplotlib.pyplot as plt
import numpy as np
import tifffile as tf

"""PART I: Processes Raw Hyperspectral Imagery (HSI) 
   ------------------------------------------------------------
   Input: .hsi & .hdr files
   Output: .npy & .png files
"""

hsi_path = '[where your .hsi file sits]'
hdr_path = '[where your .hdr file sits]'
output_hsi_npy_path = '[where you want the output .npy file of the image to sit]'
output_hsi_png_path = '[where you want the output .png file of the image to sit]'

img = envi.open(hdr_path, hsi_path)
data_spy = img.load()

data_numpy = np.nan_to_num(np.array(data_spy))
np.save(output_hsi_npy_path, data_numpy)

# Be sure to find out the spectral bands corresponding to colors red, green, and blue
r_band_index, g_band_index, b_band_index = 0, 0, 0

false_color_img = np.dstack([
    data_numpy[:, :, r_band_index],
    data_numpy[:, :, g_band_index],
    data_numpy[:, :, b_band_index]]) 
 
plt.imsave(output_hsi_png_path, false_color_img)

"""PART II: Processes Raw Binary Labeled Mask
   ------------------------------------------------------------
   Input: .tif file
   Output: .npy & .png files
"""

mask_tif_path = '[where your labeled mask file (.tif) sits]'
output_mask_npy_path = '[where you want the output .npy file of the labeled mask to sit]'
output_mask_png_path = '[where you want the output .png file of the labeled mask to sit]'

# Load the .tif file directly into a NumPy array
mask_array = tf.imread(mask_tif_path) 
mask_array = np.where(mask_array == 255, 1, mask_array)
mask_array = mask_array.astype(int)

np.save(output_mask_npy_path, mask_array)
plt.imsave(output_mask_png_path, mask_array, cmap='viridis')



    
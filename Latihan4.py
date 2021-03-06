from PIL import Image, ImageEnhance
import numpy as np


img = Image.open('Fernanda.jpg')
print(img.format)
print(img.size)
print(img.mode)

arr = np.array(img.copy())
print(type(arr))
print(arr.shape)

arrFactor1 = arr.copy()
arrFactor2 = arr.copy()
arrFactor3 = arr.copy()
arrFactor4 = arr.copy()

for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
        arrFactor1[y, x] = [max(int(arr[y, x, 0]*0.8),0),
                            max(int(arr[y, x, 1]*0.8),0),
                            max(int(arr[y, x, 2]*0.8),0)]
        arrFactor2[y, x] = [max(int(arr[y, x, 0]*0.9),0),
                            max(int(arr[y, x, 1]*0.9),0),
                            max(int(arr[y, x, 2]*0.9),0)]
        arrFactor3[y, x] = [min(int(arr[y, x, 0]*1.2),255),
                            min(int(arr[y, x, 1]*1.2),255),
                            min(int(arr[y, x, 2]*1.2),255)]
        arrFactor4[y, x] = [min(int(arr[y, x, 0]*1.3),255),
                            min(int(arr[y, x, 1]*1.3),255),
                            min(int(arr[y, x, 2]*1.3),255)]
        
Image.fromarray(np.hstack((arrFactor1, arrFactor2,arr,arrFactor3, arrFactor4))).show()

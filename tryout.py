import PIL
from PIL import ImageEnhance
from PIL import Image
from PIL import ImageFilter
import numpy as np

image = Image.open("/home/stillerf/virtpython/testbild.jpg")
#image.show("Original")

# Change Brightness: value between 0.1 and 4 makes sense
enhancer = ImageEnhance.Brightness(image)
augmented_image = enhancer.enhance(1)
#augmented_image.show("Changed Brightness")

# Change Contrast: value between 0.1 and 5 or 6 makes sense
enhancer = ImageEnhance.Contrast(augmented_image)
augmented_image = enhancer.enhance(1)
#augmented_image.show("Changed Contrast")

# Change Sharpness
enhancer = ImageEnhance.Sharpness(augmented_image)
augmented_image = enhancer.enhance(1)
#augmented_image.show("Changed Sharpness")

# Apply filter for gaussian blur
bild = augmented_image.filter(ImageFilter.GaussianBlur(0))
#bild.show("Applied gaussian blur filter")

# Apply gaussian noise
image_array = np.asarray(image)
mean = 0
sigma = 40
noise = sigma * np.random.randn(np.shape(image_array)[0],np.shape(image_array)[1],np.shape(image_array)[2]) + mean
image_array = image_array + noise
new_image = Image.fromarray(np.uint8(image_array))
#new_image.show()

# Salt and Pepper noise
image_array = np.asarray(image)
image_array.setflags(write=1)
percentage = 0.05
columns = np.shape(image_array)[0]
rows = np.shape(image_array)[1]
num_pixeltochange = columns * rows * percentage / 2

counter = num_pixeltochange
while counter > 1:
    x = np.random.randint(0,columns)
    y = np.random.randint(0,rows)
    image_array[x,y,:] = 255
    counter = counter -1

counter = num_pixeltochange
while counter > 1:
    x = np.random.randint(0,columns)
    y = np.random.randint(0,rows)
    image_array[x,y,:] = 0
    counter = counter -1


new_image = Image.fromarray(np.uint8(image_array))
new_image.show()

a = np.arange(0,27)
a = a.reshape(3,3,3)
a[2,2,] = 0

print(a)









#print(image_array)



#image.show()
#row,col,ch= image.shape

#print(sigma)
# gauss = np.random.normal(mean,sigma,(row,col,ch))
# gauss = gauss.reshape(row,col,ch)
#image = image + gauss
#image.show()

# im1 = im.filter(ImageFilter.BLUR)
# im2 = im.filter(ImageFilter.MinFilter(3))
# im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)


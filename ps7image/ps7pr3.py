#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images
#%%

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def bw(pixels, threshold):
    """ Tuning a image to black and white
    """
    output = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            if brightness(pixels[i][j]) > threshold:
                output[i][j] = [255,255,255]
            else:
                output[i][j] = [0,0,0]
    return output

# pixels = load_pixels('spam.png')
# bw_spam = bw(pixels, 100)
# save_pixels(bw_spam, 'bw_spam.png')
# compare_images('bw_spam.png', 'bw_expected.png')

#%%
def upside_down(pixels):
    """ Turning a image upside down
    """
    output = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels)):
        i_reverse = len(pixels) - i - 1
        for j in range(len(pixels[i])):
            output[i][j] = pixels[i_reverse][j]
    return output

# pixels = load_pixels('spam.png')
# ud_pixels = upside_down(pixels)
# save_pixels(ud_pixels, 'ud_spam.png')
# compare_images('ud_spam.png', 'ud_expected.png')

#%%
def reflect(pixels):
    """ Reflect a image left to right
    """
    output = create_green_image(len(pixels), len(pixels[0]))
    for i in range(len(pixels)):
        # Left half stay the same
        for j in range(len(pixels[i]) // 2):
            output[i][j] = pixels[i][j]
        # Right half reflect the left
        for j in range(len(pixels[i]) // 2, len(pixels[i])):
            j_reverse = len(pixels[i]) - j - 1
            output[i][j] = pixels[i][j_reverse]
    return output


# pixels = load_pixels('spam.png')
# reflected = reflect(pixels)
# save_pixels(reflected, 'refl_spam.png')
# compare_images('refl_spam.png', 'refl_expected.png')
# pixels = load_pixels('bu.png')
# reflected = reflect(pixels)
# save_pixels(reflected, 'refl_bu.png')
# compare_images('refl_bu.png', 'refl_bu_expected.png')

#%%
def shrink(pixels):
    """ Shrink the image 2 times, by skip every other pixel in each row and col
    """
    output = create_green_image(len(pixels) // 2, len(pixels[0]) // 2)
    for i in range(len(pixels) // 2):
        for j in range(len(pixels[i]) // 2):
            output[i][j] = pixels[i * 2][j * 2]
    return output


# pixels = load_pixels('spam_two.png')
# shrunk = shrink(pixels)
# save_pixels(shrunk, 'shrunk_spam_two.png')
# compare_images('shrunk_spam_two.png', 'shrunk_expected.png')

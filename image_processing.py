import random
import numpy as np
import skimage.io as io

# Note: Do not put any code between these functions.
# Keep all testing code at the bottom of the file.

def denoise(filename):
    
    index = 0 
    for i in range(len(filename)): # to where to slice the string
        if filename[i] == ".":
            index = i
    images = []
    for n in range(20): # insert 20 images into a list
        images.append(io.imread((filename[:index]+"_{}"+filename[index:]).format(n)))
    
    for image in images:
        height = image.shape[0]
        width = image.shape[1]
        color = image.shape[2]
    
    denoised_image = np.zeros((height, width, color)) # create a array which has the same dimension as th images
    
    for r in range(height):
        for c in range(width):
            red = 0
            green = 0
            blue = 0
            
            count = 0 # to store the number of pixels that are not white
            for image in images:
                if image[r,c][0] != 255 or image[r,c][1] != 255 or image[r,c][2] != 255: # check if the pixel is white
                    count +=1
                    red += image[r,c][0]
                    green += image[r,c][1]
                    blue += image[r,c][2]
            
            if count != 0: # to avoid ZeroDivisionError
                r_avg = red/count
                g_avg = green/count
                b_avg = blue/count
                
                denoised_image[r,c][0] = r_avg
                denoised_image[r,c][1] = g_avg
                denoised_image[r,c][2] = b_avg       
                
            else: # if the pixel of all 20 pictures at this region is white, set this pixel to be black
                
                denoised_image[r,c][0] = 0
                denoised_image[r,c][1] = 0
                denoised_image[r,c][2] = 0
            
            
    return denoised_image

def add_random_white_pixels(filename, whiteout_prob):
    
    image = io.imread(filename)
    
    height = image.shape[0]
    width = image.shape[1]
    
    probability = np.random.random((height,width)) # create an array with the same dimension 
    
    for r in range(height):
        for c in range(width):
            if probability[r,c] < whiteout_prob: # find which pixel to change into white
                image[r,c][0] = 255
                image[r,c][1] = 255
                image[r,c][2] = 255
                
    return image    
    
    

def add_white_regions(filename, num_regions):
    
    image = io.imread(filename)
    
    height = image.shape[0]
    width = image.shape[1]
    
    for n in range(num_regions):
        pos_r = random.randint(0,height) # get the postion of the up-left corner of the white region
        pos_c = random.randint(0,width)
        
        random_h = random.randint(1,height//4)
        random_w = random.randint(1,width//4)
        
        if pos_r+random_h+1 < height: # check if it is out of bound
            pos_r_to = pos_r+random_h+1
        else:
            pos_r_to = height
            
        if pos_c+random_w+1 < width:  # check if it is out of bound
            pos_c_to = pos_c+random_w+1
        else:
            pos_c_to = width
        
        for r in range(pos_r,pos_r_to): # start from the random postion  
            for c in range(pos_c,pos_c_to):
                image[r,c][0]=255
                image[r,c][1]=255
                image[r,c][2]=255
                        
    return image

import numpy as np
import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The path to the image.")
ap.add_argument("-t", "--threshold", default=100, help="Threshold to compare the images against.")
ap.add_argument("-v", "--verbose", default=False)
args = vars(ap.parse_args())

def info(msg):
    if args["verbose"]:
        print("[INFO] " + msg)
        
def find_avg_brightness(image):
    # Convert the image to HSV as the V channel gives us the brighness
    image_hsv = image.convert("HSV")
    
    total_area = image_hsv.size[0] * image_hsv.size[1]
    brightness = np.sum((np.asarray(image_hsv)[:,:,2]))
    
    return brightness / total_area

info("Loading Image...")
image = Image.open(args["image"])

info("Converting to HSV and extracting average brightness...")
avg_brightness = find_avg_brightness(image)

info("Average Brightness is: {}".format(avg_brightness))

if avg_brightness > args["threshold"]:
    print("Day")
else:
    print("Night")

Auto Day/Night Detector
=======================

Takes one required and two optional arguments:

	-i | --image: String. Path to the image.
	-t | --threshold: Integer. Threshold value above which an image is considered to be bright enough to be classified as Day. Default is 100.
	-v | --verbose: Boolean. Default False. If True, prints step by step details.

Example Usage:
    python day_night.py -i "day.jpg"

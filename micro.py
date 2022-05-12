# Course: CS361 - Software Engineering 1
# Author: Jana Dalyn Boyd
# Assignment: Microservice
# Description: Writes the URL of a random image to a text file.

import random

# repeat while site is live
while True:
    
    # look for run command
    instruct_file = open("instructions.txt", "r")
    if instruct_file.readline() == 'run':
        
        # hold urls
        all_images = {}

        # count the urls 
        image_file = open("racquet_image.txt", "r")
        url_count = len(image_file.readlines()) # Referenced: PYnative article 'Python Count Number of Lines in a File'

        # add urls to dictionary
        with open("racquet_image.txt", "r") as image_file:
            for line in image_file:
                curr_line = line.strip()
                all_images[url_count] = curr_line
                url_count -= 1

        image_file.close()

        # generate random number
        random.seed(a=None, version=2)
        ran_num = random.randint(1, len(all_images))

        # open file & write URL
        img_url = open("img_url.txt", "w")
        img_url.write(all_images[ran_num])
        img_url.close()
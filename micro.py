import random

# repeat while site is live
while True:
    
    # look for run command
    instruct_file = open("instructions.txt", "r")
    if instruct_file.readline() == 'run':
        
        # generate random number
        random.seed(a=None, version=2)
        ran_num = random.randrange(10)
 
        # URL to where images are
        file_path = 'C:\Oregon State\CS 361\Main Project\static\images{}.jpg'.format(ran_num)

        # open file & write URL
        img_url = open("img_url.txt", "w")
        img_url.write(file_path)
        img_url.close()
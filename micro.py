import random

def get_image():
    """Generates the url of a random raquet image and writes it to a text file."""

    # Generate random number
    random.seed(a=None, version=2)
    ran_num = random.randrange(10)

    # TODO update depending on number of images      
    if ran_num >= 4:
        ran_num = ran_num % 4
        
    # update to URL where images are
    file_path = 'C:\Oregon State\CS 361\Main Project\static\images{}.jpg'.format(ran_num)
    
    # open file 
    img_url = open("img_url.txt", "w")
    # write to file
    img_url.write(file_path)
    # close file 
    img_url.close()
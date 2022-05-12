Files Included (place in the same directory as your main project)

micro.py
    looks for the word 'run in a file named 'instructions.txt,'
    generated a random number, uses that number to choose a random image,
    writes the url of that image to a file named 'img_url.txt'

instructions.txt
    your main project file should write the word 'run' to this file when it needs an image url
    'micro.py' will read the word 'run' and do the above actions

img_url.txt
    'micro.py' will write the url of the image to be displayed to this file
    your main project file should read the url

Example of code that needs to be included in your main project.

    # ask microservice for url for display image
    instruct_file = open("instructions.txt", "w")
    instruct_file.write("run")
    instruct_file.close()
    
    # read url from microservice
    img_url = open("img_url.txt", "r")
    display_image = img_url.readline()
    img_url.close()
    
    # clear instruction file
    instruct_file = open("instructions.txt", "w")
    instruct_file.truncate()
    instruct_file.close()
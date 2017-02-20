import urllib
import time
import shutil
import requests
from selenium import webdriver

driver = webdriver.Chrome()
currentLoop = 185

def get_image():
    adImage = driver.find_elements_by_css_selector('.rg_l')

    # Get the image URL
    href = adImage[0].get_attribute('href')
    imgURL = href.split('imgurl=', 1)[1]
    imgURL = imgURL.split('&imgrefurl=', 1)[0]
    imgURL = imgURL.replace('%2F', '/').replace('%3A', ':')
    print imgURL
    time.sleep(1);

    # Create unique filenames
    global currentLoop
    currentLoop += 1
    # print "Current loop is " + str(currentLoop)
    image_name = str(currentLoop) + ".png"

    # Download the image
    response = requests.get(imgURL, stream=True)
    with open(image_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    time.sleep(1)

# Create an array from the .txt file
with open("ads.txt") as f:
    for line in f:
        query = line.rstrip('\n') + " logo"
        print query
        # Search on Google Images for the search term
        url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
        driver.get(url)
        time.sleep(2);
        get_image()

driver.quit()

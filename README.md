# Facebook-ads-swap

**A chrome extension that plasters your Facebook account with ads.** The chrome extension swaps all the pictures in your Facebook feed with the logos of the advertisers that currently have your contact information.

##Instructions

**How to set it up (quick)**
If you'd like to try out this extension without scraping your own Facebook advertisements, do the following:
* After cloning this repo, open the folder "extension". This is the actual chrome extension.
* Create a folder "images" in that folder. Add however many images you'd like, naming them "1.png", "2.png", etc.
* In content.js, change line 11 so that X is the number of photos that are in your "images" folder:
var random = Math.floor(Math.random() * X) + 1
* In a Chrome browser, go to the url chrome://extensions/ and click "Load unpacked extension." Add the folder "extensions".
* Browse Facebook and watch as your images get swapped.

**How to set it up (long)**
If you'd like to try out this extension by scraping your own Facebook advertisements, do the following:
* First, you need to download your entire Facebook archive. Follow the steps here:
* Go to the file "Ads.htm" and copy the list of advertisers and save it as "ads.txt"
* After installing pip dependencies and activating the virtualenv, run the python script scrape.py to scrape images from Google Images.
* Save all the images into a folder "images" and place into the folder "extension". This is the actual chrome extension.
* In content.js, change line 11 so that X is the number of photos that are in your "images" folder:
var random = Math.floor(Math.random() * X) + 1
* In a Chrome browser, go to the url chrome://extensions/ and click "Load unpacked extension." Add the folder "extensions".
* Browse Facebook and watch as your images get swapped.

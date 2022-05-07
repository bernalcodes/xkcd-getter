#!/usr/bin/env python3


# dependencies used for this project
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
from pathlib import Path
from datetime import date


# path to browser driver and folder to store images
PATH = "/home/felipe/Desktop/software/browser/chromedriver_linux64/chromedriver"
download_path = "/home/felipe/Desktop/various/various_pics/daily_xkcd/"

op = webdriver.ChromeOptions()
op.add_argument('headless')
wd = webdriver.Chrome(PATH,options=op)


# function to randomize and retrieve url to comic 
def get_xkcd(wd):
    url = "https://xkcd.com/"
    wd.get(url)
    wd.find_element(By.XPATH,".//a[@href='//c.xkcd.com/random/comic/']").click()
    image_url = wd.find_element(By.XPATH,".//img[@style='image-orientation:none']").get_attribute("src")
    return image_url


# function to download comic and save it to specified folder
def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name
        potential_path = Path(file_path)

        if potential_path.exists():
            print(f'{file_name} already exists')
        else:
            with open(potential_path,"wb") as f:
                image.save(f,"PNG")
            print(f'Success saving {file_name}')
        image.show(potential_path)
    except Exception as e:
        print(f'FAILED - {e}')


# function to log into txt file date and filename per comic downloaded
def log(file_name):
    with open("/home/felipe/Desktop/personal/personal_software/python/xkcd_getter/log.txt","a") as f:
        f.write(f'{file_name}_{date.today()}\n')
    f.close()


# main function
def main():
    url = get_xkcd(wd)
    file_name = url[29:]
    print(file_name)
    download_image(download_path,url,file_name)
    log(file_name)
    print("Done")


if __name__ == '__main__':
    main()
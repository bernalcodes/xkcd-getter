# xkcd comic downloader

This is a personal python project I developed after learning a little bit of web scraping. In few words: it goes to [xkcd.com](https://www.xkcd.com/), randomizes the comic shown, saves it and displays it on desktop. Kinda proud of it. :)

<img align="center" alt="import antigravity" src="https://imgs.xkcd.com/comics/python.png">

## Dependencies required

In this case, the dependencies used are saved in the [`requirements.txt`](./requirements.txt) file within this repo, so you can install them using `pip`:

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
from pathlib import Path
from datetime import date
```

## Usage

Within the code you can find two specific variables which are:

```
PATH = "/home/felipe/Desktop/software/browser/chromedriver_linux64/chromedriver"
download_path = "/home/felipe/Desktop/various/various_pics/daily_xkcd/"
with open("/home/felipe/Desktop/personal/personal_software/python/xkcd_getter/log.txt","a") as f:
```

In these you'll have to configure the path to the chrome webdriver, the path to the folder were you'll store the comic and the path to the log.txt file for logging
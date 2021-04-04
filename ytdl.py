#!/usr/bin/python3

import pafy, os, subprocess
from pytube import YouTube

url = input("Enter the youtube video url: ")
# url = 'https://www.youtube.com/watch?v=qvu4nPMyl3U'

try:
    v = pafy.new(url)
    # v = YouTube(url)
except ValueError:
    url = input("Enter a valid URL: ")
    v = pafy.new(url)
except Exception as e:
    print(f"something went wrong: {e}")
# print(v.streams.filter(type='video',res='1080p').download())
# print(v.streams.get_highest_resolution())
# quit()
print(f"\n\t** Downloading {v.title} **\n")
os.chdir("D:\\")
if "Youtube Video Downloads" not in os.listdir():
    os.mkdir("Youtube Video Downloads")
os.chdir("Youtube Video Downloads")
v.getbest().download()
print("Your file is downloaded in \" D:\\Youtube Video Downloads \"")

n = input("\nEnter:\n  1 - Open video folder\n  2 - Play the downloaded video: ")
if n == "1":
    subprocess.call(['explorer','.'])
elif n=='2':
    file = ''
    for i in os.listdir():
        if v.title in i:
            file = i
    os.startfile(file)
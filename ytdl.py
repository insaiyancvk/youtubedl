import pafy, os, re, urllib,glob, subprocess

def get_url(s):
    """
    Give a video ID as an argument to this function. It returns top n (7 by default) video URLs.
    """

    query = "https://www.youtube.com/results?search_query="+urllib.parse.quote(s)
    baseurl = "https://www.youtube.com/watch?v="
    response = urllib.request.urlopen(query)
    html = response.read()
    video_ids = re.findall(r"watch\?v=(\S{11})", html.decode())
    urls = []
    j = 0
    for i in video_ids:
        try:
            pafy.new(baseurl+i)
            urls.append(baseurl+i)
            j+=1
            if j==7:
                break
        except:
            continue
    return urls
print("\n\t **Note** - You can enter a search word or paste the url itself (for best results)\n")
s = input("Enter the search word: ")
urls = get_url(s)
print(f"\nHere are the top 7 search results for {s}. Enter the serial number to download it.\n")
s = s.replace(" ","+")
j=1
for i in urls:
    if len(urls) == 0:
        print("\nThere were no results :(\nmaybe try checking the spelling of the song\n")
        quit()
    try:
        v = pafy.new(i)
        print(f"{j} - {v.title}  ({v.duration})")
        j+=1
    except:
        j+=1
        continue
c = int(input("\nEnter the serial number: "))
ffmpeg = os.getcwd()+"\\ffmpeg.exe"
os.chdir("D:\\")
if "Youtube Video Downloads" not in os.listdir():
    os.mkdir("Youtube Video Downloads")
os.chdir("Youtube Video Downloads")

stream = pafy.new(urls[c-1])
t = stream.title
t = t.replace("\\"," ").replace("/"," ").replace(":"," ").replace("*"," ").replace("?"," ").replace("\""," ").replace("<"," ").replace(">"," ").replace("|"," ")
print(f"\n\t** Downloading {t} **\n")
streams = stream.videostreams[::-1]
for i in streams:
    if '1080' in str(i):
        i.download("vtemp.mp4")
        break
    elif '720' in str(i):
        i.download("vtemp.mp4")
        break
    elif '480' in str(i):
        i.download("vtemp.mp4")
        break
    elif '360' in str(i):
        i.download("vtemp.mp4")
        break
stream.getbestaudio().download("atemp.mp3")
subprocess.call([ffmpeg,'-hide_banner','-i',"atemp.mp3",'-b:a', '320k',"natemp.mp3"])
os.remove("atemp.mp3")
subprocess.call([ffmpeg,'-hide_banner','-i','vtemp.mp4','-i','natemp.mp3','-c:v', 'copy', '-c:a', 'mp3',t+".mp4"])
os.remove("vtemp.mp4")
os.remove("natemp.mp3")
print("\n\n\t***** Your file is downloaded in \" D:\\Youtube Video Downloads \"***** \n\n")

n = input("\nEnter:\n  1 - Open video folder\n  2 - Play the downloaded video: ")
if n == "1":
    os.startfile(".")
elif n=='2':
    os.startfile(max(glob.glob("./*"),key = os.path.getctime))
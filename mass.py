import json
import youtube_dl
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
with open('final.json', 'r') as myfile:
    obj = json.load(myfile)

count=1;
video_url = 'https://www.youtube.com/watch?v=qZ8Qflpn_ZU'
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([video_url])

print("Done and Dusted")

for item in obj:
	count+=1
	print(obj[item]['Start Time'])
	print(obj[item]['End Time'])
	start = 10
	end = 100
	count1=str(count)
	ffmpeg_extract_subclip("/home/shriram/Uable.mkv", start,end, targetname="mama"+count1+".mp4")
	


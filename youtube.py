# importing packages
from pytube import YouTube
import os
import subprocess

# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', new_file,
                 base+'.wav'])

# convert mp3 to wav from command 
# ffmpeg -i coolin.mp3 coolin2.wav

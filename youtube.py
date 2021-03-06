from pytube import YouTube
import os
import csv_read_write
# url input from user
saved = csv_read_write.getdict()

def download_audio(url):
    if url in saved:
        print(url + " was already downloaded.")
        return
    yt = YouTube(url)
  
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
  
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = "./audio_downloads"
  
    # download the file
    out_file = video.download(output_path=destination)
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    csv_read_write.add(url,new_file)
    # result of success
    print(yt.title + " has been successfully downloaded.")

download_audio("www.youtube.com/watch?v=vCOXTEzfoJ4")
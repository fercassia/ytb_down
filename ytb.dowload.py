import subprocess
import youtube_dl

    #Download and convert to mp3 and store ub donwloads folder
def run():

    #Ask the user for the video they want to download
    video_url = input("Insira a URL de link do video que você quer baixar: \n")

    #Download and convert to mp3 and store ub donwloads folder
    #The download=False i want to get only information about of video, and not want to downloaded now.
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url, download = False
    )
    filename = f"{video_info['title']}.mp3"
    options =  {
        'format': 'bestaudio/best',
        'keepvideo': False, #Here i  telling to him that i just want only audio after the convertion
        'outtmpl': filename, #Default name of video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] #This code is responsible to converting the video to the mp3->it's processing function - yb_dl will download the video and the post-processing will convert that video
    }
    #Download the video
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


        # Open the file once it has been downloaded
    subprocess.call(["open", filename])

if __name__ == '__main__':
    run()
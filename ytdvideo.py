from tkinter import *
from tkinter import ttk
from pytube import YouTube

def download_video():
    url = entry.get()
    resolution = combobox.get()
    if url:
        try:
            yt = YouTube(url)
            if resolution == "Highest":
                stream = yt.streams.get_highest_resolution()
            elif resolution == "Audio Only":
                stream = yt.streams.get_audio_only()
            else:
                stream = yt.streams.get_by_resolution(resolution)
            
            if stream:
                stream.download()
                print("Download completed!")
            else:
                print("Requested stream not available")
        except Exception as e:
            print(f"An error occurred: {e}")

# Configure GUI
root = Tk()
root.geometry("320x240")
root.title("ytdvideo")
root.configure(background='black')

# Add widgets
Label(root, text="Link to Video:", bg='black', fg='white').place(x=10, y=60)
entry = Entry(root, width=40)
entry.place(x=95, y=60)

res = StringVar()
combobox = ttk.Combobox(root, textvariable=res)
combobox['values'] = ('360p', '480p', '720p', '1080p', 'Highest', 'Audio Only')
combobox.place(x=100, y=100)

button = Button(root, text='Download Video', command=download_video)
button.place(x=110, y=150)

root.mainloop()
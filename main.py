from tkinter import *
from tkinter import filedialog,messagebox
from pytube import YouTube,Playlist
import os

#functionality Part

def download():
    got_path=filedialog.askdirectory()
    link_url=text.get()

    if check.get()==1:

        yt=YouTube(link_url)
        yt.streams.get_highest_resolution().download(got_path)
        messagebox.showinfo('Success','Downloading is succesfull')
        os.startfile(got_path)

    if check.get()==2:
        yt_playlist=Playlist(link_url)
        for videos in yt_playlist.videos:
            videos.streams.get_highest_resolution().download(got_path)

        messagebox.showinfo('Success','Complete Playlist is downloaded succesfully')
        os.startfile(got_path)



# GUI Part
root = Tk()

root.title('Youtube Downloader')
root.config(bg='red4')

outerframe = Frame(root, bd=5)
outerframe.grid(row=0, column=0, pady=30, padx=30)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(outerframe, image=logoImage)
logoLabel.grid(row=0, column=0, pady=20)

innerframe = LabelFrame(outerframe, text='DOWNLOAD', font=('arial black', 14, 'bold'))
innerframe.grid(row=1, column=0, pady=30)
radioImage = PhotoImage(file='video.png')
check=IntVar()
videoradioButton = Radiobutton(innerframe, image=radioImage, text='  Single Video', compound=LEFT,variable=check,value=1,
                               font=('arial', 12, 'bold')
                               , relief='solid')
videoradioButton.grid(row=0, column=0, padx=20, pady=20)

playlistImage = PhotoImage(file='playlist.png')
playlistradioButton = Radiobutton(innerframe, image=playlistImage, text='  Playlist', compound=LEFT,variable=check,value=2,
                                  font=('arial', 12, 'bold')
                                  , relief='solid')
playlistradioButton.grid(row=0, column=1, padx=20, pady=20)

text = StringVar()
url_entryField = Entry(outerframe, width=60, font=('arial', 14, 'bold'), justify=CENTER, textvariable=text, fg='gray')
url_entryField.grid(row=2, column=0, padx=10, pady=30)
text.set('Enter URL')


def click(event):
    url_entryField.delete(0, END)
    url_entryField.config(fg='black')


url_entryField.bind('<Button-1>', click)

downloadImage = PhotoImage(file='download.png')
downloadButton = Button(outerframe, image=downloadImage, bg='red4',command=download)
downloadButton.grid(row=3, column=0, pady=30)

root.mainloop()

## TODO: Another way
# from pytube import YouTube

# link = input("Enter the youtube link here:\n")

# you_tube = YouTube(link)

# print(f"\nTitle: {you_tube.title}")

# print(f"\nRating: {you_tube.rating}")

# print(f"\nViews: {you_tube.views}")

# print(f"\nVideo Length: {you_tube.length} seconds")

# print(f"\nDiscription: {you_tube.description}\n")

# video = you_tube.streams.get_highest_resolution()

# print("downloading...")

# video.download()

# print("Download complete!")

## TODO: Another
# from tkinter import *
# from tkinter import filedialog
# from moviepy.editor import *
# from moviepy.editor import VideoFileClip
# from pytube import YouTube

# import shutil


# #Functions
# def select_path():
#     #allows user to select a path from the explorer
#     path = filedialog.askdirectory()
#     path_label.config(text=path)

# def download_file():
#     #get user path
#     get_link = link_field.get()
#     #get selected path
#     user_path = path_label.cget("text")
#     screen.title('Downloading...')
#     #Download Video
#     mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
#     vid_clip = VideoFileClip(mp4_video)
#     vid_clip.close()
#     #move file to selected directory
#     shutil.move(mp4_video, user_path)
#     screen.title('Download Complete! Download Another File...')

# screen = Tk()
# title = screen.title('Youtube Download')
# canvas = Canvas(screen, width=500, height=500)
# canvas.pack()

# #image logo
# logo_img = PhotoImage(file='yt.png')
# #resize
# logo_img = logo_img.subsample(2, 2)
# canvas.create_image(250, 80, image=logo_img)

# #link field
# link_field = Entry(screen, width=40, font=('Arial', 15) )
# link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

# #Select Path for saving the file
# path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
# select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
# #Add to window
# canvas.create_window(250, 280, window=path_label)
# canvas.create_window(250, 330, window=select_btn)

# #Add widgets to window
# canvas.create_window(250, 170, window=link_label)
# canvas.create_window(250, 220, window=link_field)

# #Download btns
# download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
# #add to canvas
# canvas.create_window(250, 390, window=download_btn)

# screen.mainloop()
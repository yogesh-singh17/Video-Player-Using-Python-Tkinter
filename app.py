from tkinter import *
import cv2
from PIL import ImageTk, Image
from tkinter import messagebox
import imageio

video_name=""
pause=False
image=""

# Functions
def stream(label):
    global delay,video,screen,image
    if pause==False:

        try:
            image = video.get_next_data()
        except:
            video.close()
            return
        label.after(delay, lambda: stream(label))
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
        # print(video_name)
    else:
        image = video.get_next_data()

# Play video Function
def play_video():
    global delay,video
    global screen
    video_name=video_link.get()
    video = imageio.get_reader(video_name)
    delay = int(1000 / video.get_meta_data()['fps'])
    # print(video_name)
    screen.after(delay, lambda: stream(screen))

# Pause video function
def pause_video():
    global pause
    pause=True


def resume_video():
    global image,pause,screen
    pause=False
    stream(screen)


root=Tk()
root.title("Video Player By Yogeshwar")
root.geometry("1350x670")
root.configure(bg="#fc466b")


# Screen
screen=Label(root)
screen.pack()


# Play Button
btn_play=Button(root, text="Play",command=play_video, width=10,height=2,bg="#fdbb2d",font=("Courier", 14,"bold"))
btn_play.place(x=400,y=580)

# Pause Button
btn_pause=Button(root, text="Pause",command=pause_video, width=10,height=2,bg="#fdbb2d",font=("Courier", 14,"bold"))
btn_pause.place(x=600,y=580)

# Resume Button
btn_resume=Button(root, text="Resume",command=resume_video, width=10,height=2,bg="#fdbb2d",font=("Courier", 14,"bold"))
btn_resume.place(x=800,y=580)

# Label
label = Label(root, text="Enter Video Link")
label.config(font=("Courier", 14,"bold"))
label.place(x=10,y=595)

# Entry Box
video_link=Entry(root,width=30,bd=5)
video_link.place(x=200,y=595)


root.mainloop()



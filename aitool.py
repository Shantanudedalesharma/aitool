from Tkinter import *
from gtts import gTTS
import playsound
from PIL import Image, ImageTk
master=Tk()
master.title('Text TO Speech Tool')
image = Image.open("aliens.jpg")
photo = ImageTk.PhotoImage(image)
label1 = Label(image=photo)
label1.image = photo

photo = ImageTk.PhotoImage(image)
e=Entry(master)
e.pack()


def d():
	mytext = str(e.get())
  	language = 'en'
  	shantanu = gTTS(text=mytext, lang=language, slow=False) 
  	shantanu.save("welcome.mp3")
	playsound.playsound('/home/shantanu/welcome.mp3')

#res = Label(master)
#res.pack()
widget=Button(None,bg='gray',text='Convert Text to Speech',height=20,width=500, command=d)



widget.pack()
label1.pack()
master.mainloop()

#!/usr/local/bin/python
from Tkinter import *
#Consideraciones Previas en Debian Tener instalado lo siguiente: 
# python 2.7, python-tk , youtube-dl	
#To install youtube-dl	 it right away for all UNIX users (Linux, OS X, etc.) type: 
# sudo curl https://yt-dl.org/downloads/2015.03.03.1/youtube-dl -o /usr/local/bin/youtube-dl
# sudo chmod a+x /usr/local/bin/youtube-dl
from subprocess import *
class MyApp:

	def __init__(self, myParent):
		self.myContainer1 = Frame(myParent)
		self.myContainer1.pack()
		self.txt0 = Label(self.myContainer1)
		self.txt0["text"]= "Pegue la direccion del video (por ejemplo):"
		self.txt0.pack()
		self.txt1 = Label(self.myContainer1)
		self.txt1["text"]= "https://www.youtube.com/watch?v=JGw1FRCpL94"
		self.txt1.pack()
		self.txt2 = Entry(self.myContainer1,width=40)
		self.txt2.pack()
		self.button1 = Button(self.myContainer1)
		self.button1["text"]= "Descargar"
		self.button1.config(command=self.downloader)
		self.button1.pack()
		
	def downloader(self):
		download=self.txt2.get()
		videostring="youtube-dl -x --audio-format mp3 "+download
		result = Popen(videostring, shell=True, stdout=PIPE)
		texto=""
		texto2=""
		self.scrollbar = Scrollbar(self.myContainer1)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.listbox = Listbox(self.myContainer1, yscrollcommand=self.scrollbar.set)
		for i in result.stdout:
			textout=i.decode(sys.getdefaultencoding()).rstrip()
			texto=texto+str(i)+"\n"
			texto2=str(i)+"\n"
			self.listbox.insert(END, str(textout))
		self.listbox.pack(fill=BOTH)	
		self.txt3 = Label(self.myContainer1)
		self.txt3["text"]= "Descargado: "+texto2
		self.txt3.pack()
		self.button2 = Button(self.myContainer1)
		self.button2["text"]= "Salir"
		self.button2.config(command=quit)
		self.button2.pack()
root = Tk()
root.title("Descargar mp3 de youtube")
root.geometry("450x350")
myapp = MyApp(root)
root.mainloop()

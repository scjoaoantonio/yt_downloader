from tkinter import *
from tkinter import Tk, StringVar, ttk
import youtube_dl

cor1 = "#d3d3d3"  # cinza claro
cor2 = "#a0a0a0"  # cinza escuro


# Adicionar LINK na lista
def addlink():
    if(len(str(vnovolink.get())) > 0):
        lb_links.insert(END, vnovolink.get())
        vnovolink.delete(0, END)
    else:
        print("Tente novamente")


def downloadVideo(links):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download(links)


def removelink():
    lb_links.delete(lb_links.curselection())


def baixarLista():
    listalinks.append(str(lb_links.get(ACTIVE)))
    downloadVideo(listalinks)


app = Tk()
app.title("yt_downloader")
app.geometry("400x450")
app.resizable(width=FALSE, height=FALSE)
style = ttk.Style(app)
style.theme_use("clam")

listalinks = []
space = Label(app)
space.pack()

title = Label(app, text="Youtube Downloader",
              anchor=NW, font=('Verdana 20 bold'))
title.pack()

lb_links = Listbox(app, width=50)
for links in listalinks:
    lb_links.insert(END, links)
lb_links.pack()

space = Label(app)
space.pack()

btn_link = Button(app, text="Download",
                  command=baixarLista, width=20, bg=cor2)
btn_link.pack()

space = Label(app)
space.pack()

btn_remove_link = Button(app, text="Remover",
                         command=removelink, width=20, bg=cor1)
btn_remove_link.pack()

space = Label(app)
space.pack()

addlabel = Label(app, text="Insira o link do video aqui: ")
addlabel.pack()

vnovolink = Entry(app, width=24)
vnovolink.pack()

space = Label(app)
space.pack()

btn_inserirlink = Button(
    app, text="Adicionar link", command=addlink, width=20, bg=cor1)
btn_inserirlink.pack()


app.mainloop()

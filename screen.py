from tkinter import *
import youtube_dl


def addlink():
    lb_links.insert(END, vnovolink.get())


def downloadVideo(links):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download(links)


def baixarLista():
    listalinks.append(str(lb_links.get(ACTIVE)))
    downloadVideo(listalinks)


app = Tk()
app.title("Youtube Downloader")
app.geometry("500x300")

listalinks = []

lb_links = Listbox(app)
for links in listalinks:
    lb_links.insert(END, links)
lb_links.pack()

btn_link = Button(app, text="Download",
                  command=baixarLista)
btn_link.pack()

vnovolink = Entry(app)
vnovolink.pack()
btn_inserirlink = Button(
    app, text="Adicionar link", command=addlink)
btn_inserirlink.pack()


app.mainloop()

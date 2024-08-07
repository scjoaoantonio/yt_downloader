import re
import threading
import yt_dlp as youtube_dl
from tkinter import *
from tkinter import ttk

cor1 = "#d3d3d3"  # Cinza claro
cor2 = "#a0a0a0"  # Cinza escuro

# Adicionar LINK no listbox
def addlink():
    link = vnovolink.get().strip()
    if len(link) > 0:
        lb_links.insert(END, link)
        vnovolink.delete(0, END)
        error_label.config(text="Erro")
    else:
        error_label.config(text="O link não pode estar vazio.")

# Remover LINK do listbox
def removelink():
    selected = lb_links.curselection()
    if selected:
        lb_links.delete(selected[0])
        error_label.config(text="Erro")

# Carregamento da barra de progresso
def progress_hook(d):
    print(d)  # Debug: Print the status dictionary
    if d['status'] == 'downloading':
        percent = d['_percent_str']
        # Remove any ANSI color codes
        percent = re.sub(r'\x1b\[.*?m', '', percent)
        # Remove any non-numeric characters except the decimal point
        percent = ''.join([i for i in percent if i.isdigit() or i == '.'])
        percent = float(percent.strip())
        varBarra.set(percent)
    elif d['status'] == 'finished':
        varBarra.set(100)

# Download de vídeo da lista
def download_video(links):
    error_label.config(text="")
    for link in links:
        try:
            ydl_opts = {
                'noplaylist': True,
                'progress_hooks': [progress_hook],
                'no_color': True
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading: {link}")
                ydl.download([link])
        except Exception as e:
            error_label.config(text=f"Erro ao baixar {link}: {e}")
            print(f"Erro ao baixar {link}: {e}")

# Função chamada ao clicar no botão "Download"
def baixar_lista():
    listalinks = [lb_links.get(i) for i in lb_links.curselection()]
    if listalinks:
        varBarra.set(0)
        threading.Thread(target=download_video, args=(listalinks,), daemon=True).start()
    else:
        error_label.config(text="Nenhum vídeo selecionado para download.")
        print("Nenhum vídeo selecionado para download.")  # Debug: Print no video selected

# Configuração da tela do app
app = Tk()
app.title("yt_downloader")
app.geometry("500x550")
app.resizable(width=FALSE, height=FALSE)
style = ttk.Style(app)
style.theme_use("clam")

# Custom Style para a ProgressBar
style.configure("green.Horizontal.TProgressbar",
                troughcolor='white',
                background='green')

# Layout do aplicativo
frame = Frame(app, bg=cor1, padx=10, pady=10)
frame.pack(fill=BOTH, expand=True)

title = Label(frame, text="Youtube Downloader", font=('Verdana 20 bold'), bg=cor1)
title.pack(pady=(10, 20))

lb_links = Listbox(frame, width=60, height=15, selectmode=MULTIPLE)
lb_links.pack(pady=(0, 20))

vnovolink = Entry(frame, width=50)
vnovolink.pack(pady=(0, 10))

btn_add_link = Button(frame, text="Adicionar link", command=addlink, width=20, bg=cor2)
btn_add_link.pack(pady=(0, 5))

btn_remove_link = Button(frame, text="Remover link", command=removelink, width=20, bg=cor1)
btn_remove_link.pack(pady=(0, 10))

btn_download = Button(frame, text="Download", command=baixar_lista, width=20, bg=cor2)
btn_download.pack(pady=(0, 20))

error_label = Label(frame, text="", fg="red", bg=cor1)
error_label.pack(pady=(10, 0))

varBarra = DoubleVar()
varBarra.set(0)
pb = ttk.Progressbar(app, variable=varBarra, maximum=100, style="green.Horizontal.TProgressbar")
pb.place(x=0, y=530, width=500, height=20)

app.mainloop()

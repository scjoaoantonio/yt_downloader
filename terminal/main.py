import yt_dlp as youtube_dl  # Use yt-dlp instead of youtube_dl

link = []

def add_video():
    link.append(input("Link do video para baixar:\n"))

def remove_video():
    print(link)
    try:
        index = int(input("Digite o numero do video a ser removido:\n"))
        if 0 <= index < len(link):
            link.pop(index)
            print(link)
        else:
            print("Número inválido")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def view_videos():
    print(link)

def download_video():
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Adjust format if needed
        'noplaylist': True,  # Ensure only individual videos are downloaded
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video_link in link:
            try:
                ydl.download([video_link])
            except Exception as e:
                print(f"Erro ao baixar {video_link}: {e}")

def menu():
    op = int(input("\n(1) Adicionar video\n(2) Remover video\n(3) Ver lista para download\n(4) Baixar os videos\n(0) Sair\n-> "))
    match op:
        case 1:
            add_video()
        case 2:
            if len(link) > 0:
                remove_video()
            else:
                print("\nNão há videos na lista para remover")
        case 3:
            if len(link) > 0:
                view_videos()
            else:
                print("\nNão há videos na lista para ver")
        case 4:
            if len(link) > 0:
                download_video()
            else:
                print("\nNão há videos na lista para baixar")
        case 0:
            print("Programa finalizado")
            exit()
        case _:
            print("\nValor inválido")

while True:
    menu()

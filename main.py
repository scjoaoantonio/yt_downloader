import youtube_dl

link = []


def add_video():
    link.append(input("Link do video para baixar:\n"))


def remove_video():
    print(link)
    link.pop(int(input("Digite o numero do video a ser removido:\n")))
    print(link)


def view_videos():
    print(link)


def download_video():
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download(link)


def menu():
    op = int(input("\n(1) Adicionar video\n(2) Remover video\n(3) Ver lista para download\n(4) Baixar os videos\n(0) Sair\n-> "))
    match op:
        case 1:
            add_video()
        case 2:
            if (len(link) > 0):
                remove_video()
            else:
                print("\nNão há videos na lista para remover")
                menu()
        case 3:
            if (len(link) > 0):
                view_videos()
            else:
                print("\nNão há videos na lista para ver")
                menu()
        case 4:
            if (len(link) > 0):
                download_video()
            else:
                print("\nNão há videos na lista para baixar")
                menu()

        case 0:
            print("Programa finalizado")
            exit()

        case _:
            print("\nValor inválido")
            menu()


while True:
    menu()

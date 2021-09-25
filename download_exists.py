import os
from time import sleep
from pathlib import Path
from file_utilities import make_folder


class DownloadExists:

    def __init__(self):
        self.counter = 0

    def arquivos(self):
        downloads_path = str(Path.home() / "Downloads")
        os.chdir(downloads_path)
        lista = os.listdir()

        for arquivo in lista:
            sleep(0.5)
            self.check_file(arquivo)
        if self.counter > 0:
            print("\n")
            print(f'Foram movidos {self.counter} arquivos')
        else:
            print("\n")
            print('Não há arquivos para serem movidos.')
        sleep(3)

    def check_file(self, arquivo):
        pastas = ['Programacao', 'Textos', 'Pdf', 'Musica', 'Imagens', 'Videos', 'Documentos', 'Planilhas', 'Apresentacoes', 'Executaveis', 'Arquivos ZIP']
        if arquivo.lower().endswith(('.py', '.cs', '.js', '.php', '.html', '.sql', '.css')):
            path_to_folder = make_folder('Programacao')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith('.txt'):
            path_to_folder = make_folder('Textos')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith('.pdf'):
            path_to_folder = make_folder('Pdf')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith('.mp3'):
            path_to_folder = make_folder('Musica')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.png', '.jpg', '.bmp', '.gif', '.raw')):
            path_to_folder = make_folder('Imagens')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.mov', '.mp4', '.avi', '.flv')):
            path_to_folder = make_folder('Videos')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.doc', '.docx')):
            path_to_folder = make_folder('Documentos')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.xls', '.xlsx')):
            path_to_folder = make_folder('Planilhas')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.ppt', '.pptx')):
            path_to_folder = make_folder('Apresentacoes')
            self.move_download_exists(arquivo, path_to_folder)
            return
        elif arquivo.lower().endswith(('.exe', '.msi')):
            path_to_folder = make_folder('Executaveis')
            self.move_download_exists(arquivo, path_to_folder)
            return

        elif arquivo.lower().endswith(('.rar', '.zip', '.7z')):
            path_to_folder = make_folder('Arquivos ZIP')
            self.move_download_exists(arquivo, path_to_folder)
            return
        else:
            if arquivo not in pastas:
                path_to_folder = make_folder('Outros Arquivos')
                self.move_download_exists(arquivo, path_to_folder)
                return

    def move_download_exists(self, arquivo, path_to_new_folder):
        try:
            os.rename(f"{arquivo}", f"{path_to_new_folder}/{arquivo}")
            self.counter += 1
        except:
            pass


download_exist = DownloadExists()
download_exist.arquivos()

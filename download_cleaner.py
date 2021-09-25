import time

from past.builtins import execfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_utilities import *
from download_exists import *
import os


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        pastas = ['Programacao', 'Textos', 'Pdf', 'Musica', 'Imagens', 'Videos', 'Documentos', 'Planilhas',
                  'Apresentacoes', 'Executaveis', 'Arquivos ZIP']
        if os.path.isdir(event.src_path):
            return
        if is_code_file(event):
            path_to_folder = make_folder('Programacao')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_text_file(event):
            path_to_folder = make_folder('Textos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_pdf_file(event):
            path_to_folder = make_folder('Pdf')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_mp3_file(event):
            path_to_folder = make_folder('Musica')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_image_file(event):
            path_to_folder = make_folder('Imagens')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_video_file(event):
            path_to_folder = make_folder('Videos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_doc_file(event):
            path_to_folder = make_folder('Documentos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_spreadsheet_file(event):
            path_to_folder = make_folder('Planilhas')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_presentation_file(event):
            path_to_folder = make_folder('Apresentacoes')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        elif is_executable_file(event):
            path_to_folder = make_folder('Executaveis')
            move_to_new_corresponding_folder(event, path_to_folder)
            return
        else:
            if event not in pastas:
                path_to_folder = make_folder('Outros Arquivos')
                move_to_new_corresponding_folder(event, path_to_folder)
                return

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


downloads_path = str(Path.home() / "Downloads")
download_exists = DownloadExists()
download_exists.arquivos()

file_change_handler = Handler()
observer = Observer()
os.chdir(downloads_path)
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

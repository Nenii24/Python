from mp3 import DownloaderModel
from tkinter import messagebox

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = DownloaderModel()

    def descargar(self, url):

        if not url.strip():
            messagebox.showwarning("Aviso", "Tienes que poner una URL")
            return

        try:
            messagebox.showinfo("Inicio", "Iniciando descarga..")

            self.model.descargar_mp3(url)

            messagebox.showinfo("Descarga correcta", "Descarga completa c:")

        except Exception as e:
            messagebox.showerror("Error", str(e))
from mp3 import DownloaderModel
from tkinter import messagebox

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = DownloaderModel()

    def descargar(self, url):

        if not url.strip():
            messagebox.showwarning("Warning", "Enter a URL")
            return

        try:
            messagebox.showinfo("Starting", "Starting download..")

            self.model.descargar_mp3(url)

            messagebox.showinfo("Download succesful", "Download finished c:")

        except Exception as e:
            messagebox.showerror("Error", str(e))
#view.py
import tkinter as tk
import sys
import os



def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS  # cuando es .exe
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class AppView:


    
    def __init__(self, controller):
        self.controller = controller

        self.ventana = tk.Tk()
        self.ventana.title("MP3 DOWNLOADER <3")
        self.ventana.geometry("500x200")
        self.ventana.resizable(False, False)
        ruta_icono = resource_path("assets/icono.ico")
        self.ventana.iconbitmap(ruta_icono)

        self.miFrame = tk.Frame(self.ventana, width=500, height=600)
        self.miFrame.pack()

        self.labelTitulo = tk.Label(
            self.miFrame,
            text="Enter the URL",
            font=("Times New Roman", 15)
        )
        self.labelTitulo.place(x=180, y=50)

        self.cuadroURL = tk.Entry(self.miFrame, width=60)
        self.cuadroURL.place(x=60, y=100)

        self.btnLimpiar = tk.Button(
            self.miFrame,
            text="Clear",
            command=self.limpiar_estado
        )
        self.btnLimpiar.place(x=150, y=150)

        self.btnDescarga = tk.Button(
            self.miFrame,
            text="Download",
            command=self.click_descargar
        )
        self.btnDescarga.place(x=300, y=150)
        

    def click_descargar(self):
        url = self.cuadroURL.get()
        self.controller.descargar(url)
    
    def limpiar_estado(self):
        self.cuadroURL.delete(0, tk.END)

    def iniciar(self):
        self.ventana.mainloop()
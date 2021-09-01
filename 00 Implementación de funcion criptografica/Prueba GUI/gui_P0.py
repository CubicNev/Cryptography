# ---- Imports ---- #
from tkinter import *
from tkinter import filedialog


class Ui():

    def __init__(self):
        self.archivo = NONE

        # Inicio la ventana
        self.ventana = Tk()
        # Configuro la ventana
        self.ventana.title("Practica 0")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap("cryptography.ico")

        # Creo el contenedor
        self.contenedor = Frame(self.ventana)
        self.contenedor.pack()

        # Inserto componentes
        # -- Labels -- #
        self.label = Label(self.contenedor, text="Archivo:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.lNomArchivo = Label(self.contenedor)
        self.lNomArchivo.grid(row=0, column=1, sticky="W", padx=10, pady=10)

        # -- Botones -- #
        self.btnEscogerArchivo = Button(
            self.contenedor, text="Escoger Archivo", command=self.abrirArchivo)
        self.btnEscogerArchivo.grid(row=1, column=0, padx=10, pady=10)

        self.btnCifrar = Button(
            self.contenedor, text="Cifrar", command=self.cifrar)
        self.btnCifrar.grid(row=2, column=0, sticky="W", padx=10, pady=10)

        self.btnCifrar = Button(
            self.contenedor, text="Decifrar", command=self.decifrar)
        self.btnCifrar.grid(row=2, column=1, sticky="W", padx=10, pady=10)

        # Ejecuto la ventana
        self.ventana.mainloop()

    def abrirArchivo(self):
        # Traigo la ruta del archivo con una ventana para seleccionar archivos
        rutaArchivo = filedialog.askopenfilename(title="Selecciona un archivo .txt", 
                                                 initialdir="./..", 
                                                 filetypes=(("Archivos de texto", "*.txt"), 
                                                 ("Todos los archivos", "*.*")))
        # Abro la ruta de la imagen
        self.archivo = open(rutaArchivo, 'r')
        print(self.archivo.read())
        self.archivo.close()
        # self.lNomArchivo.config(text=str(self.archivo))

    def cifrar(self):
        if self.archivo is NONE:
            print("Selecciona primero un archivo")
        else:
            print("Cifrar")

    def decifrar(self):
        if self.archivo is NONE:
            print("Selecciona primero un archivo")
        else:
            print("Decifrar")


ui = Ui()

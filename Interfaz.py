import tkinter as tk
ventana = tk.Tk()
BotonAgregarIMG = tk.PhotoImage(file="imagenes/botonAgregar.png")
BotonEliminarIMG = tk.PhotoImage(file="imagenes/botonEliminar.png")
BotonVisualizarIMG = tk.PhotoImage(file="imagenes/botonVisualizar.png")
ventana.geometry("1280x720")
ventana.title("Arte Helado")
ventana.iconbitmap("imagenes/logoSinTexto.ico")
FondoIMG = tk.PhotoImage(file="imagenes/PantallaDeFondo.png")
Fondo = tk.Frame(ventana)
Fondo.config(bg="white")
Fondo.pack(expand=1, fill='both')

FondoIMG = tk.PhotoImage(file="imagenes/PantallaDeFondo.png")
ImagenFondo = tk.Label(Fondo)
ImagenFondo.config(image=FondoIMG)
ImagenFondo.place_configure(relheight=1, relwidth=1)
ContenedorBotones = tk.Frame(ImagenFondo, bg='#E01631')
BotonAgregar = tk.Button(ContenedorBotones)

BotonAgregar.config(image= BotonAgregarIMG, borderwidth=0)
BotonEliminar = tk.Button(ContenedorBotones)
BotonEliminar.config(image= BotonEliminarIMG, borderwidth=0)
BotonVisualizar = tk.Button(ContenedorBotones)
BotonVisualizar.config(image= BotonVisualizarIMG, borderwidth=0)


def MenuPrincipal():
    ContenedorBotones.pack()
    BotonAgregar.pack()
    BotonEliminar.pack()
    BotonVisualizar.pack()
    
def Finalizar():
    ventana.mainloop()


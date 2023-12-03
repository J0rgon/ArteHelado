
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1280x720")

icono = tk.PhotoImage(file="imagenes/logoSinTexto.png")
FondoIMG = tk.PhotoImage(file="imagenes/PantallaDeFondo.png")
BotonAgregarIMG = tk.PhotoImage(file="imagenes/botonAgregar.png")
BotonEliminarIMG = tk.PhotoImage(file="imagenes/botonEliminar.png")
BotonVisualizarIMG = tk.PhotoImage(file="imagenes/botonVisualizar.png")

ventana.title("Arte Helado")
ventana.iconphoto(True, icono)

Fondo = tk.Frame(ventana)
Fondo.config(bg="white");
Fondo.pack(expand=1, fill='both')
ImagenFondo = tk.Label(Fondo)
ImagenFondo.config(image=FondoIMG)
ImagenFondo.place_configure(relheight=1, relwidth=1)

ContenedorBotones = tk.Frame(ImagenFondo)
ContenedorBotones.grid_columnconfigure(1, uniform="group1")

ContenedorBotones.grid_rowconfigure(1)
ContenedorBotones.place_configure(relheight=1, relwidth=0.4, x=0, y=0)

BotonAgregar = tk.Button(ContenedorBotones)
BotonAgregar.config(image= BotonAgregarIMG, borderwidth=0)
BotonAgregar.grid(column=1, row=1, sticky="snew")
BotonEliminar = tk.Button(ContenedorBotones)
BotonEliminar.config(image= BotonEliminarIMG, borderwidth=0)
BotonEliminar.grid(column=1, row=2, sticky="snew")
BotonVisualizar = tk.Button(ContenedorBotones)
BotonVisualizar.config(image= BotonVisualizarIMG, borderwidth=0)
BotonVisualizar.grid(column=1, row=3, sticky="snew")



ventana.mainloop()



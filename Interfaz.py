import tkinter as tk
import Back as sql



ventana = tk.Tk()
SaborActual = ''
volumenActual = ''
BotonAgregarIMG = tk.PhotoImage(file="imagenes/botonAgregar.png")
BotonEliminarIMG = tk.PhotoImage(file="imagenes/botonEliminar.png")
BotonVisualizarIMG = tk.PhotoImage(file="imagenes/botonVisualizar.png")
BotonReporteIMG = tk.PhotoImage(file="imagenes/botonReporte.png")
BotonRegistroIMG = tk.PhotoImage(file="imagenes/botonRegistro.png")
Lupa = tk.PhotoImage(file="imagenes/lupa.png")

def OcultarTodo():
    for widget in ventana.winfo_children():
        widget.place_forget()
    ImagenFondo.place_configure(relheight=1, relwidth=1)

ventana.geometry("1280x720")
ventana.title("Arte Helado")
ventana.iconbitmap("imagenes/logoSinTexto.ico")

FondoIMG = tk.PhotoImage(file="imagenes/PantallaDeFondo.png")
Fondo = tk.Frame(ventana)
Fondo.config(bg="white")
Fondo.pack(expand=1, fill='both')



ImagenFondo = tk.Label(Fondo)
ImagenFondo.config(image=FondoIMG)
ImagenFondo.place_configure(relheight=1, relwidth=1)
Buscar = tk.Entry(ImagenFondo, font=("Verdana", 20))
ListaMovil = tk.Listbox(ImagenFondo, font=("Verdana", 20))



def MedioL(i):
	volumenActual = sql.volumenes[i]
	
BotonMedioL = tk.Button(ImagenFondo, command=MedioL(0), text=sql.volumenes[0])
BotonL = tk.Button(ImagenFondo, command=MedioL(1), text=sql.volumenes[1])
BotonGal = tk.Button(ImagenFondo, command=MedioL(2), text=sql.volumenes[2])

def RetornarNombre():
	SaborActual = Buscar.get()
	
BotonBuscar = tk.Button(image=Lupa, command=RetornarNombre())


def Scankey(event):
	val = event.widget.get()
	if val == '':
		data = sql.sabores
	else:
		data = []
		for item in sql.sabores:
			if val.lower() in item.lower():
				data.append(item)				
	Update(data)

def Update(data):
	ListaMovil.delete(0, 'end')
	# put new data
	for item in data:
		ListaMovil.insert('end', item)
		
def Desplegable():
    BotonMedioL.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.1)
    BotonL.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.3)
    BotonGal.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.5)
    BotonBuscar.place(relheight=0.2, relwidth=0.05, relx=0.5, rely=0)
    Buscar.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0)
    Buscar.bind('<KeyRelease>', Scankey)
    ListaMovil.place(relheight=0.7, relwidth=0.3, relx=0.25, rely=0.25)
    Update(sql.sabores)

def VerProductos():
    OcultarTodo()
    Desplegable()
	
def IngresarVentas():
    OcultarTodo()
    Desplegable()

BotonAgregar = tk.Button(ImagenFondo)
BotonAgregar.config(text='Agregar existencias', font=("Verdana", 20), command=IngresarVentas())
BotonEliminar = tk.Button(ImagenFondo)
BotonEliminar.config(text='Ingresar venta', font=("Verdana", 20))
BotonVisualizar = tk.Button(ImagenFondo)
BotonVisualizar.config(text='Ver existencias',command=VerProductos(), font=("Verdana", 20))
BotonReporte = tk.Button(ImagenFondo)
BotonReporte.config(text='Generar reporte', font=("Verdana", 20))
BotonRegistro = tk.Button(ImagenFondo)
BotonRegistro.config(text='Ver reportes', font=("Verdana", 20))


def Desplegable():
    OcultarTodo()
	
    BotonMedioL.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.1)
    BotonL.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.3)
    BotonGal.place(relheight=0.1, relwidth=0.1, relx=0.6, rely=0.5)
    BotonBuscar.place(relheight=0.2, relwidth=0.05, relx=0.5, rely=0)
    Buscar.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0)
    Buscar.bind('<KeyRelease>', Scankey)
    ListaMovil.place(relheight=0.7, relwidth=0.3, relx=0.25, rely=0.25)
    Update(sql.sabores)

def MenuPrincipal():
    OcultarTodo()
    BotonAgregar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0)
    BotonEliminar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.2)
    BotonVisualizar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.4)
    BotonReporte.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.6)
    BotonRegistro.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.8)
    
def Finalizar():
    ventana.mainloop()
	
# def OcultarTodo():
# 	BotonGal.place_forget()
# 	BotonL.place_forget()
# 	BotonMedioL.place_forget()
# 	BotonAgregar.place_forget()
# 	BotonBuscar.place_forget()
# 	BotonEliminar.place_forget()
# 	BotonRegistro.place_forget()
# 	BotonReporte.place_forget()
# 	BotonVisualizar.place_forget()
# 	ListaMovil.pack_forget()
# 	Buscar.place_forget()




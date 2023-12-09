import tkinter as tk
import Back as sql

ventana = tk.Tk()
SaborActual = ''
volumenActual = ''
cantidadActual = 0
venta = 0
BotonAgregarIMG = tk.PhotoImage(file="imagenes/botonAgregar.png")
BotonEliminarIMG = tk.PhotoImage(file="imagenes/botonEliminar.png")
BotonVisualizarIMG = tk.PhotoImage(file="imagenes/botonVisualizar.png")
BotonReporteIMG = tk.PhotoImage(file="imagenes/botonReporte.png")
BotonRegistroIMG = tk.PhotoImage(file="imagenes/botonRegistro.png")
Flecha = tk.PhotoImage(file="imagenes/flecha.png")
Lupa = tk.PhotoImage(file="imagenes/lupa.png")
Check = tk.PhotoImage(file="imagenes/check.png")


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
Cantidad = tk.Entry(ImagenFondo, font=("Verdana", 20))
ListaMovil = tk.Listbox(ImagenFondo, font=("Verdana", 20))

def OcultarTodo():
    for widget in ImagenFondo.winfo_children():
        widget.place_forget()

def MedioL(i):
    global volumenActual
    volumenActual = sql.volumenes[i]
    print('Volumen: ' + volumenActual)

BotonMedioL = tk.Button(ImagenFondo, command=lambda: MedioL(0), text=sql.volumenes[0])
BotonL = tk.Button(ImagenFondo, command=lambda: MedioL(1), text=sql.volumenes[1])
BotonGal = tk.Button(ImagenFondo, command=lambda: MedioL(2), text=sql.volumenes[2])

def RetornarNombre():
    global SaborActual
    SaborActual = Buscar.get()
    print(SaborActual)
      
def RetornarCant():
#    try:
        global cantidadActual
        global SaborActual
        global volumenActual
        global venta
        cantidadActual = int(Cantidad.get())
        print(cantidadActual)
        print('bool venta -> ' + str(venta))
        if venta:
            sql.RegistrarVenta(cantidadActual, SaborActual, volumenActual)
        else:
            print('Estoy dentro del else')
            sql.AgregarExistencias(cantidadActual, SaborActual, volumenActual)
        print('Estoy fuera del condicional')
        
#    except:
#        return

BotonCantidad = tk.Button(ImagenFondo, image=Check, command=lambda: RetornarCant())

def IngresarCantidad():
    OcultarTodo()
    
    Mensaje = tk.Label(ImagenFondo, text=f'{SaborActual} {volumenActual}', font=("Verdana", 20))
    Mensaje.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.3)
    Cantidad.place(relheight=0.1, relwidth=0.1, relx=0.4, rely=0.4)
    Buscar.bind('<KeyRelease>', Scankey)
    BotonCantidad.place(relheight=0.1, relwidth=0.1, relx=0.5, rely=0.4)

BotonBuscar = tk.Button(ImagenFondo, image=Lupa, command=lambda: [RetornarNombre(), IngresarCantidad()])


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
    global venta 
    venta = True
    OcultarTodo()
    Desplegable()


def AgregarExistencias():
    global venta 
    venta = False
    OcultarTodo()
    Desplegable()


BotonAgregar = tk.Button(ImagenFondo)
BotonAgregar.config(text='Agregar existencias', font=("Verdana", 20), command=lambda: IngresarVentas())
BotonEliminar = tk.Button(ImagenFondo)
BotonEliminar.config(text='Ingresar venta', font=("Verdana", 20), command=lambda: VerProductos())
BotonVisualizar = tk.Button(ImagenFondo)
BotonVisualizar.config(text='Ver existencias', font=("Verdana", 20))
BotonReporte = tk.Button(ImagenFondo)
BotonReporte.config(text='Generar reporte', font=("Verdana", 20))
BotonRegistro = tk.Button(ImagenFondo)
BotonRegistro.config(text='Ver reportes', font=("Verdana", 20))

def MenuPrincipal():
    OcultarTodo()
    BotonAgregar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0)
    BotonEliminar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.2)
    BotonVisualizar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.4)
    BotonReporte.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.6)
    BotonRegistro.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.8)
	
Regresar = tk.Button(Fondo, image=Flecha, command=lambda: MenuPrincipal())
Regresar.place(relheight=0.05, relwidth=0.05, relx=0.95, rely=0.95)
Regresar.lift()

def Finalizar():
    ventana.mainloop()



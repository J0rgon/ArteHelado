import tkinter as tk
import Back as sql
from tkinter import messagebox as mb

ventana = tk.Tk()
SaborActual = ''
volumenActual = ''
cantidadActual = 0
cantidadActualVenta = 0
venta = None
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

# 1 - Stock/Ventas
# 2, 3 - Costo/Venta

ImagenFondo = tk.Label(Fondo)
ImagenFondo.config(image=FondoIMG)
ImagenFondo.place_configure(relheight=1, relwidth=1)
Buscar = tk.Entry(ImagenFondo, font=("Verdana", 20))
Buscar3 = tk.Entry(ImagenFondo, font=("Verdana", 20))
Cantidad = tk.Entry(ImagenFondo, font=("Verdana", 20))
Cantidad2 = tk.Entry(ImagenFondo, font=("Verdana", 20))
ListaMovil = tk.Listbox(ImagenFondo, font=("Verdana", 20))
ListaMovil3 = tk.Listbox(ImagenFondo, font=("Verdana", 20))

Barra = tk.Scrollbar(ImagenFondo, orient=tk.VERTICAL)

ListaStock = tk.Canvas(ImagenFondo, bg='#69CBFF', yscrollcommand=Barra.set)

Barra.config(command=ListaStock.yview)

def OcultarTodo():
    for widget in ImagenFondo.winfo_children():
        widget.place_forget()

def RetornarNombre():
    global SaborActual
    global volumenActual
    SaborActual = Buscar.get()
    volumenActual = Buscar3.get()
    
      
def RetornarCant():
    try:
        global cantidadActual
        global SaborActual
        global volumenActual
        global venta
        cantidadActual = int(Cantidad.get())
        print(cantidadActual)
        print('bool venta -> ' + str(venta))
        if venta:
            posible = sql.RegistrarVenta(cantidadActual, SaborActual, volumenActual)
            if not posible:
                print(mb.showwarning('Alerta', 'No hay existencias suficientes'))
        else:
            print('Estoy dentro del else')
            sql.AgregarExistencias(cantidadActual, SaborActual, volumenActual)
        print('Estoy fuera del condicional')   
    except:
        mb.showwarning('Alerta', 'Cantidad ingresada no válida')
        return
    
def RetornarCantP():
    try:
         global cantidadActual
         cantidadActual = float(Cantidad.get())
         sql.ModCosto(cantidadActual, SaborActual, volumenActual)
    except:
         mb.showwarning('Alerta', 'Cantidad ingresada no válida')
         return
    
def RetornarCantV():
    try:
         global cantidadActual2
         cantidadActual2 = float(Cantidad2.get())
         sql.ModPrecio(cantidadActual2, SaborActual, volumenActual)
    except:
         mb.showwarning('Alerta', 'Cantidad ingresada no válida')
         return

BotonCantidad = tk.Button(ImagenFondo, image=Check, command=lambda: RetornarCant())
BotonCantidadP = tk.Button(ImagenFondo, image=Check, command=lambda: RetornarCantP())
BotonCantidadV = tk.Button(ImagenFondo, image=Check, command=lambda: RetornarCantV())

def IngresarCantidad():
    OcultarTodo()
    
    Mensaje = tk.Label(ImagenFondo, text=f'{SaborActual} {volumenActual}', font=("Verdana", 20))
    Mensaje.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.3)
    Cantidad.place(relheight=0.1, relwidth=0.1, relx=0.4, rely=0.4)
    BotonCantidad.place(relheight=0.1, relwidth=0.1, relx=0.5, rely=0.4)

def IngresarCantidadPV():
    OcultarTodo()
    Mensaje = tk.Label(ImagenFondo, text=f'{SaborActual} {volumenActual}', font=("Verdana", 20))
    Pago = tk.Label(ImagenFondo, text='Costo', font=("Verdana", 20))
    Venta = tk.Label(ImagenFondo, text='Venta', font=("Verdana", 20))
    Mensaje.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.3)
    Pago.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.4)
    Venta.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.5)
    Cantidad.place(relheight=0.1, relwidth=0.1, relx=0.4, rely=0.4)
    Cantidad2.place(relheight=0.1, relwidth=0.1, relx=0.4, rely=0.5)
    BotonCantidadP.place(relheight=0.1, relwidth=0.1, relx=0.5, rely=0.4)
    BotonCantidadV.place(relheight=0.1, relwidth=0.1, relx=0.5, rely=0.5)

def ObtenerVol():
     global volumenActual
     volumenProv = Buscar3.get()
     if volumenProv in sql.volumenes:
          volumenActual = volumenProv

BotonBuscar = tk.Button(ImagenFondo, image=Lupa, command=lambda: [RetornarNombre(), IngresarCantidad()])
BotonBuscar2 = tk.Button(ImagenFondo, image=Lupa, command=lambda: [RetornarNombre(), IngresarCantidadPV()])
BotonBuscar3 = tk.Button(ImagenFondo, image=Lupa, command=lambda: ObtenerVol())

def Update(data):
	ListaMovil.delete(0, 'end')
	# put new data
	for item in data:
		ListaMovil.insert('end', item)
          
def UpdateVol(data):
	ListaMovil3.delete(0, 'end')
	# put new data
	for item in data:
		ListaMovil3.insert('end', item)

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
     
def ScankeyVol(event):
	val = event.widget.get()
	if val == '':
		data = sql.volumenes
	else:
		data = []
		for item in sql.volumenes:
			if val.lower() in item.lower():
				data.append(item)				
	UpdateVol(data)


		
def Desplegable():
    SabTemp = sql.sabores
    Buscar3.place(relheight=0.2, relwidth=0.25, relx=0.6, rely=0)
    BotonBuscar.place(relheight=0.2, relwidth=0.1, relx=0.5, rely=0)
    Buscar.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0)
    Buscar.bind('<KeyRelease>', Scankey)
    Buscar3.bind('<KeyRelease>', ScankeyVol)
    ListaMovil.place(relheight=0.7, relwidth=0.25, relx=0.25, rely=0.25)
    ListaMovil3.place(relheight=0.7, relwidth=0.25, relx=0.6, rely=0.25)
    Update(sql.sabores)
    UpdateVol(sql.volumenes)

def DesplegablePV():
    Buscar3.place(relheight=0.2, relwidth=0.25, relx=0.6, rely=0)
    BotonBuscar2.place(relheight=0.2, relwidth=0.1, relx=0.5, rely=0)
    Buscar.place(relheight=0.2, relwidth=0.25, relx=0.25, rely=0)
    Buscar.bind('<KeyRelease>', Scankey)
    Buscar3.bind('<KeyRelease>', ScankeyVol)
    ListaMovil.place(relheight=0.7, relwidth=0.25, relx=0.25, rely=0.25)
    ListaMovil3.place(relheight=0.7, relwidth=0.25, relx=0.6, rely=0.25)
    Update(sql.sabores)
    UpdateVol(sql.volumenes)

Barra = tk.Scrollbar(ImagenFondo, orient=tk.VERTICAL)
ListaStock = tk.Canvas(ImagenFondo, bg='#69CBFF', yscrollcommand=Barra.set, scrollregion=(0,0,3000,3000))

def on_canvas_configure(event):
    ListaStock.configure(scrollregion=ListaStock.bbox("all"))

def VerProductos():
    global Barra
    global ListaStock
    OcultarTodo()
    Barra.config(command=ListaStock.yview)
    Barra.place(relheight=0.95, relwidth=0.02, relx=0.98, rely=0)
    Barra.lift()

    frame_inside_canvas = tk.Frame(ListaStock)
    ListaStock.create_window((0, 0), window=frame_inside_canvas, anchor=tk.NW)

    nombreH = tk.Label(frame_inside_canvas, text=('Sabor').ljust(20), font=("Verdana", 20), width=20, bg='#1cba00')
    volH = tk.Label(frame_inside_canvas, text=('Vol').ljust(10), font=("Verdana", 20), width=10, bg='#1cba00')
    existenciasH = tk.Label(frame_inside_canvas, text=('Stock').ljust(5), font=("Verdana", 20), width=5, bg='#1cba00')
    vendidoH = tk.Label(frame_inside_canvas, text=('Vend.').ljust(6), font=("Verdana", 20), width=6, bg='#1cba00')
    costoH = tk.Label(frame_inside_canvas, text=('Costo').ljust(6), font=("Verdana", 20), width=10, bg='#1cba00')
    precioH = tk.Label(frame_inside_canvas, text=('Venta').ljust(6), font=("Verdana", 20), width=10, bg='#1cba00')

    nombreH.grid(column=0, row=0)
    volH.grid(column=1, row=0)
    existenciasH.grid(column=2, row=0)
    vendidoH.grid(column=3, row=0)
    costoH.grid(column=4, row=0)
    precioH.grid(column=5, row=0)

    Todos = sql.TodosHelados()
    fila = 1
    for i, helado in enumerate(Todos):
        nombre = tk.Label(frame_inside_canvas, text=str(helado[0]).ljust(20), font=("Verdana", 20), width=20, bd=2)
        vol = tk.Label(frame_inside_canvas, text=str(Todos[i][1]).ljust(10), font=("Verdana", 20), width=10, bd=2)
        existencias = tk.Label(frame_inside_canvas, text=str(Todos[i][2]).ljust(5), font=("Verdana", 20), width=5, bd=2)
        vendido = tk.Label(frame_inside_canvas, text=str(Todos[i][3]).ljust(6), font=("Verdana", 20), width=6, bd=2)
        costo = tk.Label(frame_inside_canvas, text=str(Todos[i][4]).ljust(6), font=("Verdana", 20), width=10, bd=2)
        precio = tk.Label(frame_inside_canvas, text=str(Todos[i][5]).ljust(6), font=("Verdana", 20), width=10, bd=2)

        nombre.grid(column=0, row=fila)
        vol.grid(column=1, row=fila)
        existencias.grid(column=2, row=fila)
        vendido.grid(column=3, row=fila)
        costo.grid(column=4, row=fila)
        precio.grid(column=5, row=fila)

        fila += 1

    frame_inside_canvas.bind("<Configure>", on_canvas_configure)
    ListaStock.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def IngresarVentas():
    global venta 
    venta = True
    OcultarTodo()
    Desplegable()


def AgregarExistencias():
    global venta 
    venta = False
    print('bool venta -> previo ocultar' + str(venta))
    OcultarTodo()
    Desplegable()

def ModificarPV():
    OcultarTodo()
    DesplegablePV()

def ConfirmarRegistro():
     resultado = mb.askokcancel(title='Confirmar crear registro', message='¿Utilizar datos actuales y reiniciarlos?')
     if resultado:
          sql.GenerarRegistro()

IngresarNombre = tk.Entry(ImagenFondo, font=("Verdana", 20))

def DelSabor():
    global SaborActual
    SaborActual = IngresarNombre.get()
    if SaborActual in sql.sabores:
         print(SaborActual)
         sql.EliminarSabor(SaborActual)
         SaborActual = None
    else:
         mb.showwarning(title='No encontrado', message='Sabor no encontrado')
    return


def EliminarSabor():
    OcultarTodo()
    Situacion = tk.Label(ImagenFondo, font=("Verdana", 20), text='Eliminar')
    ConfirmarDel = tk.Button(ImagenFondo, image=Check, command=lambda:DelSabor())
    Situacion.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.3)
    IngresarNombre.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.4)
    ConfirmarDel.place(relheight=0.1, relwidth=0.1, relx=0.55, rely=0.4)
    return

def EnviarSabor():
     global SaborActual
     SaborActual = IngresarNombre.get()
     if len(SaborActual) > 20:
          mb.showerror(title='Excedido', message='Caracteres máximos excedidos')
          return
     if SaborActual not in sql.sabores:
          sql.CrearSabor(SaborActual)
     else:
          mb.showwarning(title='Ya existe', message='El sabor ya existe')
     return

def CrearSabor():
     OcultarTodo()
     Situacion = tk.Label(ImagenFondo, font=("Verdana", 20), text='Max 20 caracteres')
     Eliminar = tk.Button(ImagenFondo, text='Eliminar\nSabor', font=("Verdana", 20), command=lambda: EliminarSabor())
     Confirmar = tk.Button(ImagenFondo, image=Check, command=lambda: EnviarSabor())
     IngresarNombre.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.4)
     Confirmar.place(relheight=0.1, relwidth=0.1, relx=0.65, rely=0.4)
     Eliminar.place(relheight=0.1, relwidth=0.1, relx=0, rely=0.9)
     Situacion.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.3)

def DelVol():
    global volumenActual
    volumenActual = IngresarNombre.get()
    if volumenActual in sql.volumenes:
         sql.EliminarVol(volumenActual)
         volumenActual = None
    else:
         mb.showwarning(title='No encontrado', message='Volumen no encontrado')
    return


def EliminarVol():
    OcultarTodo()
    Situacion = tk.Label(ImagenFondo, font=("Verdana", 20), text='Eliminar')
    ConfirmarDel = tk.Button(ImagenFondo, image=Check, command=lambda:DelVol())
    Situacion.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.3)
    IngresarNombre.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.4)
    ConfirmarDel.place(relheight=0.1, relwidth=0.1, relx=0.55, rely=0.4)
    return

def EnviarVol():
     global volumenActual
     volumenActual = IngresarNombre.get()
     if len(volumenActual) > 10:
          mb.showerror(title='Excedido', message='Caracteres máximos excedidos')
          return
     if volumenActual not in sql.volumenes:
          sql.CrearVol(volumenActual)
     else:
          mb.showwarning(title='Ya existe', message='El volumen ya existe')
     return

def CrearVol():
     OcultarTodo()
     Situacion = tk.Label(ImagenFondo, font=("Verdana", 20), text='Max 10 caracteres')
     Eliminar = tk.Button(ImagenFondo, text='Eliminar\nVolumen', font=("Verdana", 20), command=lambda: EliminarVol())
     Confirmar = tk.Button(ImagenFondo, image=Check, command=lambda: EnviarVol())
     IngresarNombre.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.4)
     Confirmar.place(relheight=0.1, relwidth=0.1, relx=0.65, rely=0.4)
     Eliminar.place(relheight=0.1, relwidth=0.1, relx=0, rely=0.9)
     Situacion.place(relheight=0.1, relwidth=0.2, relx=0.35, rely=0.3)


BotonAgregar = tk.Button(ImagenFondo)
BotonAgregar.config(text='Agregar existencias', font=("Verdana", 20), command=lambda: AgregarExistencias())
BotonEliminar = tk.Button(ImagenFondo)
BotonEliminar.config(text='Ingresar venta', font=("Verdana", 20), command=lambda: IngresarVentas())
BotonVisualizar = tk.Button(ImagenFondo)
BotonVisualizar.config(text='Ver existencias', font=("Verdana", 20), command=lambda: VerProductos())
BotonReporte = tk.Button(ImagenFondo)
BotonReporte.config(text='Generar reporte', font=("Verdana", 20), command=lambda: ConfirmarRegistro())
BotonRegistro = tk.Button(ImagenFondo)
BotonRegistro.config(text='Modif. Pago/Venta', font=("Verdana", 20), command=lambda: ModificarPV())
BotonSalir = tk.Button(ImagenFondo, text='Salir', font=("Verdana", 20), command=lambda: ventana.destroy())
BotonNuevoSabor = tk.Button(ImagenFondo, text='Agregar\nsabor', font=("Verdana", 20), command=lambda: CrearSabor())
BotonNuevoVol = tk.Button(ImagenFondo, text='Agregar\nvolumen', font=("Verdana", 20), command=lambda: CrearVol())

def MenuPrincipal():
    OcultarTodo()
    global ListaStock
    global Barra
    ListaStock.pack_forget()
    Barra.place_forget()
    BotonAgregar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0)
    BotonEliminar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.2)
    BotonVisualizar.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.4)
    BotonReporte.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.6)
    BotonRegistro.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.8)
    BotonSalir.place(relheight=0.1, relwidth=0.1, relx=0, rely=0.9)
    BotonNuevoSabor.place(relheight=0.2, relwidth=0.1, relx=0, rely=0.45)
    BotonNuevoVol.place(relheight=0.2, relwidth=0.1, relx=0, rely=0.25)
	
Regresar = tk.Button(Fondo, image=Flecha, command=lambda: MenuPrincipal())
Regresar.place(relheight=0.05, relwidth=0.05, relx=0.95, rely=0.95)
Regresar.lift()

def Finalizar():
    ventana.mainloop()



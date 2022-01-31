from distutils.log import info
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import Tree
from turtle import width
from main import Classregex, Classcrud
import os


ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"
class Errorlog:
    def registroerror():
        log = open(ruta, 'a')
        print("No seleccion ninguna fila", file=log)
    def regexerrorbaja():
        log = open(ruta, 'a')
        print("Error de regex al realizar una baja", file=log)
    def regexerroralta():
        log = open(ruta, 'a')
        print("Error de regex al realizar un alta", file=log)
    def regexerrormodifica():
        log = open(ruta, 'a')
        print("Error de regex al realizar una modificacion", file=log)

 
class Ventana:
    def __init__(self, window):
        self.main = window
        self.main.title ('GESTION DE INVENTARIO')
        self.main.configure()
        self.main.geometry ('500x450')
        self.main.resizable(0,0)
        self.obj_crud = Classcrud()
        self.obj_regex= Classregex()

        # Creación de etiquetas

        self.encabezado = Label(self.main, text="Ingrese datos del producto:",
                            height=4, font=("",16))
        self.id_producto = Label(self.main, text="ID:", width=12, anchor=W,
                            font=(12))
        self.nombre_prod = Label(self.main, text="Producto:", font=(12))
        self.categoria = Label(self.main, text="Categoría:", font=(12))
        self.cantidad = Label(self.main, text="Cantidad:", font=(12))
        self.unidad = Label(self.main, text="Unidad:", font=(12))
        self.ubicacion = Label(self.main, text="Ubicación:", font=(12))

        # Ubicación de etiquetas

        self.encabezado.grid(row=0, column=0, columnspan=2, padx=10, sticky=W)
        self.id_producto.grid(row=1, column=0, padx=10, sticky=W) 
        self.nombre_prod.grid(row=2, column=0, padx=10, sticky=W)
        self.categoria.grid(row=3, column=0, padx=10, sticky=W)  
        self.cantidad.grid(row=4, column=0, padx=10, sticky=W)
        self.unidad.grid(row=5, column=0, padx=10, sticky=W)  
        self.ubicacion.grid(row=6, column=0, padx=10, sticky=W) 

        # Variables de Entries de la ventana de trabajo

        self.id_e1 = IntVar()
        self.nombre_e2 = StringVar()
        self.categoria_e3 = StringVar()
        self.cantidad_e4 = StringVar()
        self.unidad_e5 = StringVar()
        self.ubicacion_e6 = StringVar()

        # Creación de Entries

        opciones = [
                    "Ferretería",
                    "Pinturería",
                    "Jardinería",
                    "Electricidad",
                    "Herramientas",
                    "Limpieza",
                    "Gomería"
                    ]

        self.e1 = Entry(self.main,textvariable=self.id_e1, state='normal', width=40)  
        self.e2 = Entry(self.main, textvariable=self.nombre_e2, width=40)
        self.e3 = OptionMenu(self.main, self.categoria_e3, *opciones) 
        self.e4 = Entry(self.main, textvariable=self.cantidad_e4, width=40)
        self.e5 = Entry(self.main, textvariable=self.unidad_e5, width=40)
        self.e6 = Entry(self.main, textvariable=self.ubicacion_e6, width=40)

        # Configuracion del menu

        self.e3.configure(text="Elija", bg="white", width=35, relief=SUNKEN)

        # Ubicación de Entries  
        self.e1.focus()   
        self.e1.grid(row=1, column=1, ipady=2, pady=10)
        self.e2.grid(row=2, column=1, ipady=2, pady=10)
        self.e3.grid(row=3, column=1, ipady=2, pady=10)
        self.e4.grid(row=4, column=1, ipady=2, pady=10)
        self.e5.grid(row=5, column=1, ipady=2, pady=10)
        self.e6.grid(row=6, column=1, ipady=2, pady=10)

        # Creación de botones

        self.boton_alta = Button(self.main, text="ALTA", font=("",10,BOLD),
                            command=lambda: self.alta_v())
        self.boton_baja = Button(self.main, text="BAJA", font=("",10,BOLD),
                            command=lambda: self.baja_v())
        self.boton_modificar = Button(self.main, text="MODIFICAR",
                                font=("",10,BOLD), command=lambda: self.modifica_v())
        self.borrar_2_but = Button(self.main, text="LIMPIAR", font=("",10,BOLD),
                            command=lambda: self.limpiar())
        self.boton_consulta = Button(self.main, text="CONSULTAR", font=("",10,BOLD),
                                command=lambda: self.consulta_v())
        self.boton_salir = Button(self.main, text="SALIR", font=("",10,BOLD),
                            command=self.main.destroy)
        self.boton_desplegado = Button(self.main, text=">", font=("",10,BOLD),
                                command=self.desplegar)
        self.boton_plegado = Button(self.main, text="<", font=("",10,BOLD),
                                command=self.plegar)
        self.boton_showall = Button(self.main, text="VER TODO", font=("", 10, BOLD),
                        command=lambda: self.showall())
        self.boton_removeall = Button(self.main, text="LIMPIAR TODO", font=("", 10, BOLD),
                        command=lambda: self.limpiar_tree())

        # Ubicación de botones

        self.boton_alta.place(x=15, y=400)
        self.boton_baja.place(x=70, y=400)
        self.boton_modificar.place(x=125, y=400)
        self.boton_salir.place(x=400, y=400)
        self.borrar_2_but.place(x=318, y=400)
        self.boton_consulta.place(x=220, y=400)
        self.boton_desplegado.place(x=470, y=50)
        self.boton_plegado.place(x=1150, y=50)
        self.boton_showall.place(x=900, y=400)
        self.boton_removeall.place(x=700, y=400)

        #Treeview
        self.tabla = ttk.Treeview(self.main) 
        self.tabla.place(x=500, y=100)
        self.tabla['columns'] = ('ID', 'Producto', 'Categoría', 'Cantidad', 'Unidad', 'Ubicación')
        
        #Columnas
        self.tabla.column('#0', width = 0, stretch = NO)
        self.tabla.column('ID', anchor=CENTER, minwidth = 70, width = 70, stretch = True)
        self.tabla.column('Producto', minwidth = 70, width = 300, stretch = True)
        self.tabla.column('Categoría', minwidth = 70, width = 70, stretch = True)
        self.tabla.column('Cantidad', minwidth = 70, width = 70, stretch = True)
        self.tabla.column('Unidad', minwidth = 70, width = 70, stretch = True)
        self.tabla.column('Ubicación', minwidth = 70, width = 70, stretch = True)
        
        #Encabezado
        self.tabla.heading("#0", text="", anchor=CENTER)
        self.tabla.heading("ID", text="ID", anchor=CENTER)
        self.tabla.heading("Producto", text="Producto", anchor=CENTER)
        self.tabla.heading("Categoría", text="Categoría", anchor=CENTER) 
        self.tabla.heading("Cantidad", text="Cantidad", anchor=CENTER)
        self.tabla.heading("Unidad", text="Unidad", anchor=CENTER)
        self.tabla.heading("Ubicación", text="Ubicación", anchor=CENTER)

        
        def print_element(event):
         
            tree = event.widget
            valor = [tree.item(item)["values"] for item in tree.selection()]
            datos =(valor[0])
            lista_datos = datos

            #listadatos = datos.split("'")
            print(tree.selection())
            
            print(lista_datos)
            
            self.id_e1.set(lista_datos[0])
            self.nombre_e2.set(lista_datos[1])
            self.categoria_e3.set(lista_datos[2])
            self.cantidad_e4.set(lista_datos[3])
            self.unidad_e5.set(lista_datos[4])
            self.ubicacion_e6.set(lista_datos[5])
        self.tabla.bind("<<TreeviewSelect>>", print_element)
        

    def plegar(self):
        self.main.geometry ('500x450')


    def desplegar(self):
        self.main.geometry ('1180x450')  


    def alta_v(self):
        variables = [self.nombre_e2, self.categoria_e3, self.cantidad_e4, self.unidad_e5, self.ubicacion_e6]
        if self.obj_regex.check(
                            self.nombre_e2.get(),
                            self.cantidad_e4.get(),
                            self.unidad_e5.get(),
                            self.ubicacion_e6.get()
                        ) == 0:
                        self.obj_crud.alta(variables, self.tabla)
                        
                        messagebox.showinfo("Productos", "Producto registrado con éxito")
        else:
            Errorlog.regexerroralta()

    def baja_v(self):
            self.obj_crud.baja(self.tabla)
                    
            messagebox.showinfo("Productos", "Producto eliminado con éxito")
        


    def consulta_v(self):
        self.limpiar_tree()
        self.obj_crud.consulta(self.id_e1.get(), self.categoria_e3.get(), self.tabla)
  
    def showall(self):
        self.obj_crud.actualizar_treeview(self.tabla)

    def modifica_v(self):
        variables = [self.nombre_e2, self.categoria_e3, self.cantidad_e4, self.unidad_e5, self.ubicacion_e6]
        self.obj_crud.modificar(variables, self.tabla)
        messagebox.showinfo("Productos", "Producto modificado con éxito")

    def limpiar(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.categoria_e3.set("")
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)

    def limpiar_tree(self):
        filas = self.tabla.get_children()
        for items in filas:
            self.tabla.delete(items)


    

        
    
    
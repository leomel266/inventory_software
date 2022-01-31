
from logging import info
from tkinter import *
import os
from peewee import *
from db import *
from functools import wraps
from log import logger
from enum import unique
from datetime import datetime
from ast import arg



ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"
class Errorcon:
    def errorconectar():
        log = open(ruta, 'a')
        print("Error al conectarse con la base de datos", file=log)



class Crud:
    def __init__(self):
        db = SqliteDatabase('mibase.db')

    class BaseModel(Model):
        class Meta:
            database = db

    # def decora_alta (funcion):
    #         def envoltura(*arg, **kargs):
    #             print(arg[1].get(), arg[2].get())
    #             print(arg[1].get(), type(arg[2].get()))
    #             return funcion (*arg, **kargs)
            
    #         return envoltura
    def actualizar_treeview(self, tabla):
        filas = tabla.get_children()
        for items in filas:
            tabla.delete(items)
        datos = Productos.select()
        
        for fila in datos:
            tabla.insert("",'end', text=(fila.id), values = (fila.id, fila.producto, fila.categoria, fila.cantidad, fila.unidad, fila.ubicacion))
    @logger.logging
    
    def alta(self, variables, tabla):
        
        lista = []
        for variable in variables:
            lista.append(variable.get())
        #check(datos)
        producto = Productos()
        producto.producto = lista[0]
        producto.categoria = lista[1]
        producto.cantidad = lista[2]
        producto.unidad = lista[3]
        producto.ubicacion = lista[4]
        producto.save()
        self.actualizar_treeview(tabla)
        print("Registro ingresado")
        return f"""
Alta: {str(producto)}, {str(variables)}, {str(tabla)}"""

        

    @logger.logging
    def baja(self, tabla):
        item_seleccionado = tabla.focus()
        valor_id = tabla.item(item_seleccionado)
        datos = (valor_id["text"],)
        borrar = Productos.get(Productos.id == datos)
        borrar.delete_instance()
        self.actualizar_treeview(tabla)
        print("Registro borrado")
        return f"""
Baja: {item_seleccionado}, {tabla}"""
     
        
    @logger.logging
    def modificar(self, variables, tabla):
        item_seleccionado = tabla.focus()
        valor = tabla.item(item_seleccionado)
        lista = []
        for variable in variables:
            lista.append(variable.get())
        producto = Productos()
        producto.producto = lista[0]
        producto.categoria = lista[1]
        producto.cantidad = lista[2]
        producto.unidad = lista[3]
        producto.ubicacion = lista[4]
        datos = (valor["text"])
        mod = Productos.update(producto = lista[0], categoria = lista[1], cantidad = lista[2], unidad = lista[3], ubicacion = lista[4]).where(Productos.id == datos)
        mod.execute() 
        print(valor["values"])   
        self.actualizar_treeview(tabla)
        print("Registro modificado")
        return f"""
Modificación: {item_seleccionado}, {variables}, {tabla}"""
        

    def consulta(self, id, categoria, tabla):
        datos = Productos.select().where((Productos.categoria == categoria)|(Productos.id == id))
        for fila in datos:
            tabla.insert("",'end', text=(fila.id), values = (fila.id, fila.producto, fila.categoria, fila.cantidad, fila.unidad, fila.ubicacion))
  
        


    





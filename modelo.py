
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




class Crud:
    def __init__(self):
        db = SqliteDatabase('mibase.db')

    class BaseModel(Model):
        class Meta:
            database = db

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
Alta: {(lista[0])}, {(lista[1])}, Categoria {(lista[2])}, Unidad {(lista[3])}, Ubicacion {(lista[4])}"""

        

    @logger.logging
    def baja(self, tabla):
        item_seleccionado = tabla.focus()
        valor_id = tabla.item(item_seleccionado)
        datos = (valor_id["text"],)
        borrar = Productos.get(Productos.id == datos)
        borrar.delete_instance()
        self.actualizar_treeview(tabla)
        nombre=(valor_id["values"])
        print("Registro borrado")
        return f"""
Baja: {nombre}"""
     
        
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
Modificación: {(lista[0])}, {(lista[1])}, Categoria {(lista[2])}, Unidad {(lista[3])}, Ubicacion {(lista[4])}"""
        

    def consulta(self, id, categoria, tabla):
        datos = Productos.select().where((Productos.categoria == categoria)|(Productos.id == id))
        for fila in datos:
            tabla.insert("",'end', text=(fila.id), values = (fila.id, fila.producto, fila.categoria, fila.cantidad, fila.unidad, fila.ubicacion))
  
        


    





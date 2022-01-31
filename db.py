from peewee import *

try:
    db = SqliteDatabase('mibase.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class Productos(BaseModel):
        producto = CharField(unique = True)
        categoria = TextField()
        cantidad = TextField()
        unidad = TextField()
        ubicacion = TextField()   
        
    db.connect()
    db.create_tables([Productos])

except:
    print("Error al crear la base de datos.")
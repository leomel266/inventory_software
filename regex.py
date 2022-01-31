from tkinter import *
from tkinter import messagebox
import re

class Regex:
    def check(self, nombre, cantidad, unidad, ubicacion):
        self.cadena11 = nombre
        self.cadena22 = cantidad
        self.cadena33 = unidad
        self.cadena55 = ubicacion
        patron11 = "^[0-9a-zA-Z_ÑñÁáÉéÍíÓóÚú\/\" ]+$"
        patron22 = "^[0-9.,/]+$"
        patron33 = "^[0-9a-zA-Z_ÑñÁáÉéÍíÓóÚú/ ]+$"
        if (
            re.match(patron11, self.cadena11)
            and re.match(patron22, self.cadena22)
            and re.match(patron33, self.cadena33)
            and re.match(patron33, self.cadena55)
        ):
            return 0

        else:
            messagebox.showinfo(
                "Caracter inválido", "Uno o más campos poseen caracteres inválidos ó campos sin completar"
            )
            return 1
        
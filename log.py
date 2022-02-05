import logging
from tkinter import W

class LoggingManager():

    def __init__(self):
        self._logger = logging.basicConfig(
            filename="./logging.txt",
            filemode="a",
            level=logging.INFO,
            datefmt="%Y/%m/%d %H:%M:%S",
            format="%(asctime)s - %(levelname)s: %(message)s")
        self.logger = logging.getLogger()
    
    def logging(self, func):
        def wrap(*args):
            self.logger.info(f"Ejecutando método: {func.__name__}")
            resultado = func(*args)
            if resultado:
                self.logger.info(f"El método {func.__name__} retorna: {resultado}")
            else:
                self.logger.info(f"El método {func.__name__} no retorna nada.")
            self.logger.info(f"Terminó la ejecución: {func.__name__}")
        return wrap

logger = LoggingManager()
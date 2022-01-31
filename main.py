from tkinter import *
from vista import *
from modelo import *
from regex import *


class Controller:
    def __init__(self, root):
        self.main_controller = root
        self.activar_vista()
        
        
    def activar_vista(self,):
        Ventana(self.main_controller)  


if __name__=='__main__':
    main_tk = Tk()
    aplicacion = Controller(main_tk)
    
    main_tk.mainloop()

    
    
class Classregex(Regex):
    Regex()  

class Classcrud(Crud):
    Crud()



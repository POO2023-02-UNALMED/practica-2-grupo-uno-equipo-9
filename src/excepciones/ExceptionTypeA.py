from src.excepciones.ErrorAplicacion import ErrorAplicacion
class ExceptionTypeA(ErrorAplicacion):
    def __init__(self,err_input,type):
        super().__init__("Hubo un error con los tipos. Se ingreso {}, de tipo")

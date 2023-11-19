from src.excepciones.ErrorAplicacion import ErrorAplicacion


class ExceptionTypeA(ErrorAplicacion):
    def __init__(self, text):
        super().__init__("Error con el ingreso de datos: " + text)

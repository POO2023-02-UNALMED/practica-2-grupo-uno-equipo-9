from src.excepciones.ErrorAplicacion import ErrorAplicacion


class ExceptionTypeB(ErrorAplicacion):
    def __init__(self, text):
        super().__init__("Error con el procesamiento de datos: " + text)

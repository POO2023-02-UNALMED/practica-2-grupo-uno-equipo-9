class ErrorAplicacion(Exception):
    def __init__(self,text):
        super().__init__("Error en la Ejecucion: " + text)

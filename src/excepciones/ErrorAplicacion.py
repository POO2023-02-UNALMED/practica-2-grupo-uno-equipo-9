class ErrorAplicacion(Exception):
    def __init__(self,text):
        super().__init__("Manejo de errores de la Aplicación: " + text)

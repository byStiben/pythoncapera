
class Producto:
    def __init__(self, identificador, nombre, clase, precio):
        self.__identificador=identificador
        self.__nombre=nombre
        self.__clase=clase
        self.__precio=precio
    
    def setIdentificador(self, identificador):
        self.__identificador=identificador
    
    def getIdentificador(self):
        return self.__identificador
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setTipo(self, clase):
        self.__clase=clase

    def getTipo(self):
        return self.__clase
    
    def setPrecio(self,precio):
        self.__precio=precio
    
    def descuentoIndividual(self, descuento):
        self.__precio=self.__precio*descuento
   
    def descuentoEmpresa(self, descuento):
        self.__precio=self.__precio*descuento

    def getPrecio(self):
        return self.__precio 
      

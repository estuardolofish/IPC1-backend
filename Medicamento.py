class Medicamento:
    def __init__(self, idMedicamento,nombre, precio, descripcion, cantidad, top):
        
        self.idMedicamento = idMedicamento
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.top = top
  

# Get

    def getIdMedicamento(self):
        return self.idMedicamento

    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getDescripcion(self):
        return self.descripcion
        
    def getCantidad(self):
        return self.cantidad

    def getTop(self):
        return self.top

   
# Set

    def setIdMedicamento(self, idMedicamento):
        self.idMedicamento = idMedicamento

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setTop(self, top):
        self.top = top
    
    

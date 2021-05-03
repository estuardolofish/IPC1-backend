class Compra:
    def __init__(self, idCompra,usuarioPaciente, idMedicamento, cantidad):
        
        self.idCompra = idCompra
        self.usuarioPaciente = usuarioPaciente
        self.idMedicamento = idMedicamento
        self.cantidad = cantidad

# Get

    def getIdCompra(self):
        return self.idCompra

    def getUsuarioPaciente(self):
        return self.usuarioPaciente
    
    def getIdMedicamento(self):
        return self.idMedicamento

    def getCantidad(self):
        return self.cantidad
    
   
# Set

    def setIdCompra(self, idCompra):
        self.idCompra = idCompra

    def setUsuarioPaciente(self, usuarioPaciente):
        self.usuarioPaciente = usuarioPaciente
    
    def setIdMedicamento(self, idMedicamento):
        self.idMedicamento = idMedicamento
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad
    
    

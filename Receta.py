class Receta:
    def __init__(self, idFactura, fecha, nomPaciente, padecimiento, descripcion):
        
        self.idFactura = idFactura
        self.fecha = fecha
        self.nomPaciente = nomPaciente
        self.padecimiento = padecimiento
        self.descripcion = descripcion

# Get

    def getIdFactura(self):
        return self.idFactura
        
    def getFecha(self):
        return self.fecha

    def getNomPaciente(self):
        return self.nomPaciente

    def getPadecimiento(self):
        return self.padecimiento

    def getDescripcion(self):
        return self.descripcion

   

# Set



    def setIdFactura(self, idFactura):
        self.idFactura = idFactura
        
    def setFecha(self, fecha):
        self.fecha = fecha

    def setNomPaciente(self, nomPaciente):
        self.nomPaciente = nomPaciente

    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    
class FacturaServicio:
    def __init__(self, idFactura, fecha, nomPaciente, nomDoctor, consulta, operacion, internado, total):
        
        self.idFactura = idFactura
        self.fecha = fecha
        self.nomPaciente = nomPaciente
        self.nomDoctor = nomDoctor
        self.consulta = consulta
        self.operacion = operacion
        self.internado = internado
        self.total = total

# Get

    def getIdFactura(self):
        return self.idFactura
        
    def getFecha(self):
        return self.fecha

    def getNomPaciente(self):
        return self.nomPaciente

    def getNomDoctor(self):
        return self.nomDoctor

    def getConsulta(self):
        return self.consulta

    def getOperacion(self):
        return self.operacion

    def getInternado(self):
        return self.internado

    def getTotal(self):
        return self.total

# Set


    def setIdFactura(self, idFactura):
        self.idFactura = idFactura
        
    def setFecha(self, fecha):
        self.fecha = fecha

    def setNomPaciente(self, nomPaciente):
        self.nomPaciente = nomPaciente

    def setNomDoctor(self, nomDoctor):
        self.nomDoctor = nomDoctor

    def setConsulta(self, consulta):
        self.consulta = consulta

    def setOperacion(self, operacion):
        self.operacion = operacion

    def setInternado(self, internado):
        self.internado = internado

    def setTotal(self, total):
        self.total = total


    
    

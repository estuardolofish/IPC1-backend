class Cita:
    def __init__(self, idCita,usuarioPaciente, fecha, hora, motivo,estado,usuarioDoctor):
        
        self.idCita = idCita
        self.usuarioPaciente = usuarioPaciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.usuarioDoctor = usuarioDoctor

# Get

    def getIdCita(self):
        return self.idCita

    def getUsuarioPaciente(self):
        return self.usuarioPaciente
    
    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora
        
    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado

    def getUsuarioDoctor(self):
        return self.usuarioDoctor

   
# Set

    def setIdCita(self, idCita):
        self.idCita = idCita

    def setUsuarioPaciente(self, usuarioPaciente):
        self.usuarioPaciente = usuarioPaciente
    
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setHora(self, hora):
        self.hora = hora

    def setMotivo(self, motivo):
        self.motivo = motivo

    def setEstado(self, estado):
        self.estado = estado

    def setUsuarioDoctor(self, usuarioDoctor):
        self.usuarioDoctor = usuarioDoctor
    
    

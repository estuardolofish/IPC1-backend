class Usuario:
    def __init__(self, nombre, apellido, fechaNacimiento, sexo, userName, contrasenia, telefono, tipo, especialidad, top):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.sexo = sexo
        self.userName = userName
        self.contrasenia = contrasenia
        self.telefono = telefono
        self.tipo = tipo
        self.especialidad = especialidad
        self.top = top
# Get
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
        
    def getSexo(self):
        return self.sexo

    def getUserName(self):
        return self.userName

    def getContrasenia(self):
        return self.contrasenia

    def getTelefono(self):
        return self.telefono

    def getTipo(self):
        return self.tipo

    def getEspecialidad(self):
        return self.especialidad

    def getTop(self):
        return self.top

# Set

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setUserName(self, userName):
        self.userName = userName
    
    def setContrasenia(self, contrasenia):
        self.contrasenia = contrasenia

    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def setTop(self, top):
        self.top = top

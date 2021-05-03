from flask import Flask, jsonify, request
from flask_cors import CORS
from Usuario import Usuario
from Medicamento import Medicamento
from Cita import Cita
from Compra import Compra
from ContCompra import ContCompra
from FacturaServicio import FacturaServicio
from Receta import Receta
import json

app = Flask(__name__)
CORS(app)

Usuarios = []
Medicamentos = []
Citas = []
Compras = []
ContCompras = []
FacturaServicios = []
Recetas = []

# 0 = Paciente
# 1 = Doctor
# 2 = Enfermero
# 3 = Admin
Usuarios.append(Usuario("Estuardo", "Lopez", "1998-11-22", "M", "201907622", 123, 0,3,"",3 ))
Medicamentos.append(Medicamento(0, "Panadol", 1.25, "MedicinaCalmante", 50, 10))
Citas.append(Cita(0, "201907622", "2021-05-01", "10:00", "Dolor de cabeza", "Pendiente", "201907622"))
Compras.append(Compra(0,"201907622",0,5))
ContCompras.append(ContCompra(0))
FacturaServicios.append(FacturaServicio(0, "0000-00-00", "Estuardo Lopez", "Doctor", 100, 5000, 800, 5900))
Recetas.append(Receta(0,"0000-00-00","Estuardo Lopez","Apendice","operacion"))
# OPCIONES PARA USUARIO ADMINISTRADOR, DOCTORES, ENFERMERAS Y PACIENTES
# para mostrar los datos de Usuario 
@app.route('/Usuarios', methods = ['GET'])
def mostrarUsuarios():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        objeto = {
            'Nombre': usuario.getNombre(),
            'Apellido': usuario.getApellido(),
            'FechaNacimiento': usuario.getFechaNacimiento(),
            'Sexo': usuario.getSexo(),
            'UserName': usuario.getUserName(),
            'Contrasenia': usuario.getContrasenia(),
            'Telefono': usuario.getTelefono(),
            'Tipo': usuario.getTipo(),
            'Especialidad': usuario.getEspecialidad(),
            'Top':usuario.getTop()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/UsuariosTopReporte', methods = ['GET'])
def mostrarUsuariosTopReporte():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        objeto = {
            'Nombre': usuario.getNombre(),
            'Apellido': usuario.getApellido(),
            'FechaNacimiento': usuario.getFechaNacimiento(),
            'Sexo': usuario.getSexo(),
            'UserName': usuario.getUserName(),
            'Contrasenia': usuario.getContrasenia(),
            'Telefono': usuario.getTelefono(),
            'Tipo': usuario.getTipo(),
            'Especialidad': usuario.getEspecialidad(),
            'Top':usuario.getTop()
        }
        Datos.append(objeto)
    # sorted(Datos, key=lambda x: x['Top'])
    ordenados  = sorted(Datos, key=lambda Top: Top['Top'], reverse=True)
 
    print(ordenados)
    return(jsonify(ordenados))

# para crear un nuevo usuario
@app.route('/Usuarios', methods=['POST'])
def agregarUsuario():
    
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fechaNacimiento = request.json['fechaNacimiento']
    sexo = request.json['sexo']
    userName = request.json['userName']
    contrasenia = request.json['contrasenia']
    telefono = request.json['telefono']
    tipo = request.json['tipo']
    especialidad = request.json['especialidad']
    top = 0

    # for i in range(len(Usuarios)):
    for usuario in Usuarios:
        print(usuario)
        # if userName == Usuarios[i].getUserName():
        if userName == usuario.getUserName():
            return jsonify({'Mensaje':'El Nombre de Usuario ya Existe ' + usuario.getUserName(),})
    print(userName)
    print(usuario.getUserName())
    nuevo = Usuario(nombre, apellido, fechaNacimiento, sexo, userName, contrasenia, telefono, tipo, especialidad, top)
    Usuarios.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente ' + userName,})
# para mostrar un usuario especifico
@app.route('/Usuarios/<string:userName>', methods=['GET'])
def ObtenerUsuarios(userName): 
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUserName() == userName:
            objeto = {
            'Nombre': usuario.getNombre(),
            'Apellido': usuario.getApellido(),
            'UserName': usuario.getUserName(),
            'Contrasenia': usuario.getContrasenia(),
            'FechaNacimiento': usuario.getFechaNacimiento(),
            'Tipo': usuario.getTipo(),
            'Especialidad': usuario.getEspecialidad(),
            'Telefono': usuario.getTelefono(),
            'Top':usuario.getTop()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

# para modificar usuarios
@app.route('/Usuarios/<string:userName>', methods=['PUT'])
def ActualizarUsuarios(userName):
    usuarioAux = request.json['userAuxiliar']
    print(usuarioAux)
    global Usuarios
    if userName == usuarioAux:
        for i in range(len(Usuarios)):
            if usuarioAux == Usuarios[i].getUserName():
                Usuarios[i].setNombre(request.json['nombre'])
                Usuarios[i].setApellido(request.json['apellido'])
                Usuarios[i].setFechaNacimiento(request.json['fecha'])
                Usuarios[i].setContrasenia(request.json['contrasenia'])
                Usuarios[i].setEspecialidad(request.json['especialidad'])
                Usuarios[i].setTelefono(request.json['telefono'])
                return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
        return jsonify({'Mensaje':'No se encontro el dato para actualizar'})
    else:
        print("hola")
        for i in range(len(Usuarios)):
            if userName == Usuarios[i].getUserName():
                return jsonify({'Mensaje':'El usuario ya existe'})
        for i in range(len(Usuarios)):
            if usuarioAux == Usuarios[i].getUserName():
                Usuarios[i].setUserName(request.json['userName'])
                Usuarios[i].setNombre(request.json['nombre'])
                Usuarios[i].setApellido(request.json['apellido'])
                Usuarios[i].setFechaNacimiento(request.json['fecha'])
                Usuarios[i].setContrasenia(request.json['contrasenia'])
                Usuarios[i].setEspecialidad(request.json['especialidad'])
                Usuarios[i].setTelefono(request.json['telefono'])
                return jsonify({'Mensaje':'Datos Actualizados'})


# para Actualizar top
@app.route('/UsuariosTop/<string:userName>', methods=['PUT'])
def ActualizarUsuarioTop(userName):
    global Usuarios
    for i in range(len(Usuarios)):
        if userName == Usuarios[i].getUserName():
            Usuarios[i].setTop((float(Usuarios[i].getTop()) + float(request.json['top'])))
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



# para eliminar Usuarios
@app.route('/Usuarios/<string:userName>', methods=['DELETE'])
def EliminarUsuarios(userName):
    global Usuarios
    for i in range(len(Usuarios)):
        if userName == Usuarios[i].getUserName():
            del Usuarios[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})    
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
        

# -------------------------------------------------------------


# OPCIONES PARA MEDICAMENTOS
# para mostrar los datos de MEDICAMENTO
@app.route('/Medicamentos', methods = ['GET'])
def mostrarMedicamento():
    global Medicamentos
    Datos = []
    for medicamento in Medicamentos:
        objeto = {
            'IdMedicamento': medicamento.getIdMedicamento(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad(),
            'Top': medicamento.getTop()
        }
        Datos.append(objeto)
    return(jsonify(Datos))



    # para mostrar los datos de MEDICAMENTO
@app.route('/MedicamentosTopReporte', methods = ['GET'])
def mostrarMedicamentoTopReporte():
    global Medicamentos
    Datos = []
    for medicamento in Medicamentos:
        objeto = {
            'IdMedicamento': medicamento.getIdMedicamento(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad(),
            'Top': medicamento.getTop()
        }
        Datos.append(objeto)
    ordenados  = sorted(Datos, key=lambda Top: Top['Top'], reverse=True)

    print(ordenados)
    return(jsonify(ordenados))

# para crear un nuevo Medicamentos
@app.route('/Medicamentos', methods=['POST'])
def agregarMedicamento():
    idMedicC = 0
    global Medicamentos
    idMedicamento = request.json['idMedicamento']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cantidad = request.json['cantidad']
    top = 0
    for i in range(len(Medicamentos)):
        print(i)
        idMedicC  = idMedicC + 1
    nuevo = Medicamento(idMedicC, nombre, precio, descripcion, cantidad,top)
    Medicamentos.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Medicamento exitosamente '})

# para mostrar un Medicamentos especifico
@app.route('/Medicamentos/<int:id>', methods=['GET'])
def ObtenerMedicamentos(id): 
    global Medicamentos
    for medicamento in Medicamentos:
        if medicamento.getIdMedicamento() == id:
            objeto = {
            'IdMedicamento': medicamento.getIdMedicamento(),
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad(),
            'Top': medicamento.getTop()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el Medicamento"}
    return(jsonify(salida))


# para Actualizar Medicamentos
@app.route('/Medicamentos/<int:id>', methods=['PUT'])
def ActualizarMedicamento(id):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if id == Medicamentos[i].getIdMedicamento():
            Medicamentos[i].setNombre(request.json['nombre'])
            Medicamentos[i].setPrecio(request.json['precio'])
            Medicamentos[i].setDescripcion(request.json['descripcion'])
            Medicamentos[i].setCantidad(request.json['cantidad'])
           
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

# para Actualizar top
@app.route('/MedicamentosTop/<int:id>', methods=['PUT'])
def ActualizarMedicamentoTop(id):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if id == Medicamentos[i].getIdMedicamento():
            Medicamentos[i].setTop((float(Medicamentos[i].getTop()) + float(request.json['top'])))
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

# para eliminar Medicamentos
@app.route('/Medicamentos/<int:id>', methods=['DELETE'])
def EliminarMedicamentos(id):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if id == Medicamentos[i].idMedicamento:
            del Medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})    
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
        

# -------------------------------------------------------------



# OPCIONES PARA LAS CITAS
# para mostrar los datos de CITAS
@app.route('/Citas', methods = ['GET'])
def mostrarCitas():
    global Citas
    Datos = []
    for cita in Citas:
        objeto = {
            'IdCita': cita.getIdCita(),
            'UsuarioPaciente': cita.getUsuarioPaciente(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado(),
            'UsuarioDoctor': cita.getUsuarioDoctor()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

# para crear un nuevo CITA
@app.route('/Citas', methods=['POST'])
def agregarCita():
    idCitaC = 0
    global Citas
    idCitas = request.json['idCitas']
    usuarioPaciente = request.json['usuarioPaciente']
    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    estado = request.json['estado']
    usuarioDoctor = request.json['usuarioDoctor']

    # for i in range(len(Usuarios)):
    for cita in Citas:
        print(cita)
        # if userName == Usuarios[i].getUserName():
        if usuarioPaciente == cita.getUsuarioPaciente():
            if cita.getEstado() == "Pendiente" or cita.getEstado() == "Aceptada":
                return jsonify({'Mensaje':'El Usuario ' + cita.getUsuarioPaciente() + ' ya tiene una Pendiente o Aceptada ',})
    for i in range(len(Citas)):
        print(i)
        idCitaC  = idCitaC + 1
    nuevo = Cita(idCitaC, usuarioPaciente, fecha, hora, motivo, estado, usuarioDoctor)
    Citas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego La Cita exitosamente '})

@app.route('/Citas/<int:id>', methods=['PUT'])
def ActualizarCitas(id):
    global Citas
    for i in range(len(Citas)):
        if id == Citas[i].getIdCita():
            Citas[i].setUsuarioDoctor(request.json['usuarioDoctor'])
            Citas[i].setEstado(request.json['Estado'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})



# -------------------------------------------------------------
# OPCIONES PARA LAS COMPRA
# para mostrar los datos de COMPRA
@app.route('/Compras', methods = ['GET'])
def mostrarCompras():
    global Compras
    Datos = []
    for compra in Compras:
        objeto = {
            'IdCompra': compra.getIdCompra(),
            'UsuarioPaciente': compra.getUsuarioPaciente(),
            'IdMedicamento': compra.getIdMedicamento(),
            'Cantidad': compra.getCantidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

# para crear un nuevo CITA
@app.route('/Compras', methods=['POST'])
def agregarCompras():
    cont = 0
    global Compras
    global ContCompras
    idCompra = request.json['idCompra']
    usuarioPaciente = request.json['usuarioPaciente']
    idMedicamento = request.json['idMedicamento']
    cantidad = request.json['cantidad']

    for i in range(len(ContCompras)):
        print(i)
        cont  = cont + 1

    print("hola")
    print(cont)
    nuevo = Compra(cont, usuarioPaciente, idMedicamento, cantidad)
    Compras.append(nuevo)
    return jsonify({'Mensaje':'Compra ingresada '})

@app.route('/ContCompra', methods = ['GET'])
def mostrarContadorCompra():
    global ContCompras
    Datos = []
    for contcompra in ContCompras:
        objeto = {
            'cont': contcompra.getCont()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/ContCompra', methods=['POST'])
def agregarContadorCompra():
    global ContCompras
    idComprac = request.json['cont']
    nuevo = ContCompra(idComprac)
    ContCompras.append(nuevo)
    return jsonify({'Mensaje':'contador ingresado '})


# ----------------------------------------


# OPCIONES PARA GENERAR LA FACTURA
@app.route('/FacturaServicio', methods = ['GET'])
def mostrarFacturaServicio():
    global FacturaServicios
    Datos = []
    for facturaServicio in FacturaServicios:
        objeto = {
            'idFactura': facturaServicio.getIdFactura(),
            'fecha': facturaServicio.getFecha(),
            'nomPaciente': facturaServicio.getNomPaciente(),
            'nomDoctor': facturaServicio.getNomDoctor(),
            'consulta': facturaServicio.getConsulta(),
            'operacion': facturaServicio.getOperacion(),
            'internado': facturaServicio.getInternado(),
            'total': facturaServicio.getTotal()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/FacturaServicio/<int:id>', methods=['GET'])
def mostrarFacturaServicioID(id): 
    global FacturaServicios
    for facturaServicio in FacturaServicios:
        if facturaServicio.getIdFactura() == id:
            objeto = {
                'idFactura': facturaServicio.getIdFactura(),
                'fecha': facturaServicio.getFecha(),
                'nomPaciente': facturaServicio.getNomPaciente(),
                'nomDoctor': facturaServicio.getNomDoctor(),
                'consulta': facturaServicio.getConsulta(),
                'operacion': facturaServicio.getOperacion(),
                'internado': facturaServicio.getInternado(),
                'total': facturaServicio.getTotal()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el Servicio"}
    return(jsonify(salida))


# para agregar UNA NEUVA FACTAR
@app.route('/FacturaServicio', methods=['POST'])
def agregarFacturaServicio():
    idFacturaServicio = 0
    global FacturaServicios
    idFactura = request.json['idFactura']
    fecha = request.json['fecha']
    nomPaciente = request.json['nomPaciente']
    nomDoctor = request.json['nomDoctor']
    consulta = request.json['consulta']
    operacion = request.json['operacion']
    internado = request.json['internado']
    total = request.json['total']
    for i in range(len(FacturaServicios)):
        print(i)
        idFacturaServicio  = idFacturaServicio + 1
    nuevo = FacturaServicio(idFacturaServicio, fecha, nomPaciente, nomDoctor, consulta, operacion, internado, total)
    FacturaServicios.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Medicamento exitosamente '})




# -------------------------------------------------------------


# OPCIONES PARA GENERAR LA FACTURA
@app.route('/Receta', methods = ['GET'])
def mostrarReceta():
    global Recetas
    Datos = []
    for receta in Recetas:
        objeto = {
            'idFactura': receta.getIdFactura(),
            'fecha': receta.getFecha(),
            'nomPaciente': receta.getNomPaciente(),
            'padecimiento': receta.getPadecimiento(),
            'descripcion': receta.getDescripcion()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


@app.route('/Receta/<int:id>', methods=['GET'])
def mostrarRecetaID(id): 
    global Recetas
    for receta in Recetas:
        if receta.getIdFactura() == id:
            objeto = {
                'idFactura': receta.getIdFactura(),
                'fecha': receta.getFecha(),
                'nomPaciente': receta.getNomPaciente(),
                'padecimiento': receta.getPadecimiento(),
                'descripcion': receta.getDescripcion()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el Servicio"}
    return(jsonify(salida))


# para agregar UNA NEUVA FACTAR
@app.route('/Receta', methods=['POST'])
def agregarReceta():
    idFacturaReceta = 0
    global Recetas
    idFactura = request.json['idFactura']
    fecha = request.json['fecha']
    nomPaciente = request.json['nomPaciente']
    padecimiento = request.json['padecimiento']
    descripcion = request.json['descripcion']
    for i in range(len(Recetas)):
        print(i)
        idFacturaReceta  = idFacturaReceta + 1
    nuevo = Receta(idFacturaReceta, fecha, nomPaciente, padecimiento, descripcion)
    Recetas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Medicamento exitosamente '})



# ----------------------------





if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000, debug = True)
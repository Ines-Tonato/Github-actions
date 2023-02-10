
from flask import Blueprint, render_template, request , redirect, url_for
from app.data.gasto_dao import GastoDao

from app.data.user_dao import UserDao
from app.utils.db import db
from app.data.models.user import User

users = Blueprint("routes", __name__)


@users.route('/')
def home():
    user_dao = UserDao()
    users = user_dao.select_all(db)
    return render_template('index.html',users=users)

@users.route('/new' , methods=['POST'])
def add_user():
    
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    usuario=request.form['usuario']


    if nombre and apellido and usuario:
      cursor = db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
      sql = "INSERT INTO usuarios (nombre,apellido,usuario) VALUES (%s, %s, %s)"
      data = (nombre,apellido ,usuario) # HACEMOS UNA TUPLA CON LOS DATOS 
      cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
      db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO

    return redirect('/')

@users.route('/edit/<string:id_usuario>', methods=['POST','GET'])
def edit (id_usuario):

    nombre=request.form['nombre']
    apellido=request.form['apellido']
    usuario=request.form['usuario']

    if nombre and apellido and usuario:

       cursor = db.cursor() 
       sql = "UPDATE usuarios SET nombre = %s, apellido = %s, usuario = %s WHERE id_usuario = %s"
       data = (nombre,apellido ,usuario,id_usuario)
       cursor.execute(sql,data) 
       db.commit()
    return redirect(url_for('routes.home'))


@users.route('/delete/<string:id_usuario>')
def delete(id_usuario):
    cursor = db.cursor() 
    sql= "DELETE FROM gastos WHERE usuario_id=%s"
    data = (id_usuario,)
    cursor.execute(sql,data)
    sql = "DELETE FROM usuarios WHERE id_usuario=%s"
    cursor.execute(sql,data)
    db.commit() 
    return redirect(url_for('routes.home')) 



@users.route('/gastos', methods=['POST','GET'])  
def gastos():
    
    gasto_dao = GastoDao()
    gastos = gasto_dao.select_all(db)
    user_dao = UserDao()
    users = user_dao.select_all(db)
    return render_template('gastos.html',gastos=gastos, users=users) 
    
@users.route('/addgastos', methods=['POST','GET'])
def addgastos():
    
    fecha=request.form['fecha']
    descripcion=request.form['descripcion']
    cantidad=request.form['cantidad']
    usuario_id=request.form['usuario_id']


 
    cursor = db.cursor() 
    sql = "INSERT INTO gastos (fecha,descripcion,cantidad,usuario_id) VALUES (%s, %s, %s, %s)"
    data = (fecha, descripcion , cantidad, usuario_id) 
    cursor.execute(sql,data) 
    db.commit()

    return redirect(url_for('routes.gastos'))


@users.route('/deletegastos/<string:id_gasto>')
def deletegastos(id_gasto):
    cursor = db.cursor() 
    sql = "DELETE FROM gastos WHERE id_gasto=%s"
    data = (id_gasto,)
    cursor.execute(sql,data) 
    db.commit() 
    return redirect(url_for('routes.gastos')) 

@users.route('/editgastos/<string:id_gasto>', methods=['GET','POST'])
def editgastos (id_gasto):
    fecha = request.form['fecha']
    descripcion = request.form['descripcion'] 
    cantidad = request.form['cantidad'] 

    if fecha and descripcion and cantidad :
        cursor = db.cursor()
        sql = "UPDATE gastos SET fecha = %s, descripcion = %s, cantidad = %s WHERE id_gasto = %s"
        data = (fecha,descripcion,cantidad,id_gasto)
        cursor.execute(sql,data)
        db.commit()
    return redirect(url_for('routes.gastos')) 





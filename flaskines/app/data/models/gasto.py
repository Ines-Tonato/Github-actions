from datetime import date
class Gasto:
    def __init__(self, id_gasto:int, fecha: date, descripcion:str, cantidad:int, usuario_id:int):
      self.id_gasto = id_gasto
      self.fecha= fecha
      self.descripcion = descripcion
      self.cantidad = cantidad
      self.usuario_id = usuario_id
   
  

   
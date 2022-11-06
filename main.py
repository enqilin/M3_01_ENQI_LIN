
class Producto(): 
  def __init__(self,productos,precios):
    self.productos=productos
    self.precios=precios
  print("El preoductos se ha creado con éxito")
  def __str__(self):
     return"El {} vale {}".format(self.productos,self.precios)

producto1=Producto("chocolate",1.3)
producto2=Producto("calleta",1.8)
print(str(producto1))
print(str(producto2))
producto1.precios=1.45
print(str(producto1))

class alumno():
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
  print("El alumno ha sido creado con éxito.")
  def calificacion(self):
    return "El alumno {} ha aprobado con un {}" .format(self.nombre,self.nota) if self.nota >=5 else "El alumno {} ha suspendido con un {}".format(self.nombre,self.nota)

alumno1=alumno("Carlos", 8)
print(alumno.calificacion(alumno1))
alumno2=alumno("Juan" , 3)
print(alumno.calificacion(alumno2))


class alumno():
  def __init__(self, nombre, nota):
    self.nombre=nombre
    self.nota=nota
  print("El alumno ha sido creado con éxito.")
  def calificacion(self):
    if self.nota <=5:
      print("El alumno {} ha aprobado con un {}".format(self.nombre,self.nota))
    else:
      print("El alumno {} ha suspendido con un {}",format(self.nombre,self.nota))
    
  def __str__(self):
    return "el alumno {} con una nota de {}".format(self.nombre,self.nota)


alumno1=alumno("Carlos", 8)
alumno2=alumno("Juan" , 3)
print(str(alumno1))
print(str(alumno2))
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


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

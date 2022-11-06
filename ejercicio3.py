
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

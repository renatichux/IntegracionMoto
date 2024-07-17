from django.db import models

############################################################################### 

class Cliente (models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'cliente'       

class Cargo (models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=50)

    class Meta:
        db_table = 'cargo'  

class Empleado (models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    anexo = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleado'

class Boleta (models.Model):
    id_boleta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=50)
    total = models.IntegerField()

    class Meta:
        db_table = 'boleta'

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=50)
    

    class Meta:
        db_table = 'marca'

class Tipo_Moto(models.Model):
    id_tipo_moto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)


    class Meta:
        db_table = 'tipo_moto'

class Moto(models.Model):
    id_moto = models.AutoField(primary_key=True)
    id_tipo_moto = models.ForeignKey(Tipo_Moto, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    color = models.CharField(max_length=20)
    cilindrada = models.IntegerField()

    class Meta:
        db_table = 'moto'

class Detalle_Boleta (models.Model):
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    id_moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

    class Meta:
        db_table = 'detalle_boleta'        



class Carrito_Compras(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'carrito_compras'







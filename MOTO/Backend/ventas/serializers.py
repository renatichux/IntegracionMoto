from rest_framework import serializers
from .models import *

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id_marca','nombre_marca' )

class Carrito_ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito_Compras
        fields = ('id_carrito','id_cliente','id_moto','cantidad' )



class Tipo_MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Moto
        fields = ('id_tipo_moto','descripcion' )

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = ('id_moto', 'id_tipo_moto', 'id_marca', 'modelo', 'precio', 'color', 'cilindrada')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id_cliente', 'rut','nombre', 'apellido','direccion', 'telefono', 'email')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id_empleado', 'rut','nombre', 'apellido','anexo', 'email', 'id_cargo')


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('id_cargo','nombre_cargo' )



class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = ('id_boleta', 'id_cliente', 'id_empleado', 'fecha', 'total')



class Detalle_BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Boleta
        fields = ('id_detalle_boleta', 'id_boleta', 'id_moto', 'cantidad', 'precio_unitario')

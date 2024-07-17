from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
#from .models import Region,Persona,Comuna
from .models import *
#from .serializers import RegionSerializer,PersonaSerializer
from .serializers import *
from rest_framework.parsers import JSONParser, FileUploadParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK1":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK2":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK3":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)






#########################################################################
################################## MOTO ##################3##############

class MotoList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Moto.objects.all()
         serializer = MotoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = MotoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    


class MotoUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = MotoSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")


  
class MotoDetail(APIView):
    def get_object(self, pk):
        try:
            return Moto.objects.get(pk=pk)
        except Moto.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = MotoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = MotoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#########################################################################
#########################################################################





#########################################################################
################################## MARCA ################################

class MarcaList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Marca.objects.all()
         serializer = MarcaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = MarcaSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class MarcaUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = MarcaSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class MarcaDetail(APIView):
    def get_object(self, pk):
        try:
            return Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = MarcaSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = MarcaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#########################################################################
#########################################################################





#########################################################################
################################# TIPO MOTO #############################
class TipoMotoList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Tipo_Moto.objects.all()
         serializer = Tipo_MotoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = Tipo_MotoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class TipoMotoUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = Tipo_MotoSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class TipoMotoDetail(APIView):
    def get_object(self, pk):
        try:
            return Tipo_Moto.objects.get(pk=pk)
        except Tipo_Moto.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = Tipo_MotoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = Tipo_MotoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################
#########################################################################





#########################################################################
################################## CARRITOO #############################

class Carrito_comrasList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Carrito_Compras.objects.all()
         serializer = Carrito_ComprasSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = Carrito_ComprasSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class Carrito_comprasUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = Carrito_ComprasSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class Carrito_comprasDetail(APIView):
    def get_object(self, pk):
        try:
            return Carrito_Compras.objects.get(pk=pk)
        except Carrito_Compras.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = Carrito_ComprasSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = Carrito_ComprasSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################




#########################################################################
################################### CLIENTE #############################

class ClienteList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Cliente.objects.all()
         serializer = ClienteSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = ClienteSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class ClienteUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = ClienteSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = ClienteSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = ClienteSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################



#########################################################################
################################## EMPLEADO #############################

class EmpleadoList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Empleado.objects.all()
         serializer = EmpleadoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = EmpleadoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class EmpleadoUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = EmpleadoSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class EmpleadoDetail(APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = EmpleadoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = EmpleadoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################

#########################################################################
################################## CARGO ################################

class CargoList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Cargo.objects.all()
         serializer = CargoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = CargoSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class CargoUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = CargoSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class CargoDetail(APIView):
    def get_object(self, pk):
        try:
            return Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = CargoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = CargoSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################





#########################################################################
################################## BOLETA ###############################

class BoletaList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Boleta.objects.all()
         serializer = BoletaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = BoletaSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class BoletaUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = BoletaSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class BoletaDetail(APIView):
    def get_object(self, pk):
        try:
            return Boleta.objects.get(pk=pk)
        except Boleta.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = BoletaSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = BoletaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################





#########################################################################
############################# DETALLE BOLETA ############################

class Detalle_BoletaList(APIView):
    # MOSTRAR TODOS
    def get(self, request, format=None):
         registro = Detalle_Boleta.objects.all()
         serializer = Detalle_BoletaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    # INSERTAR UNO
    def post(self, request, format=None):
        #print("1,Post",request)
        data = JSONParser().parse(request)
        #print("1",data)
        registro = Detalle_BoletaSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
    
class Detalle_BoletaUpload(APIView):
    # INSERTAR DESDE UN ARCHIVO
    def post(self, request, format=None):
        file = request.FILES['file']
        data = JSONParser().parse(file)
        errores = []
        registros_exitosos = []

        for registro in data:
            serializer = Detalle_BoletaSerializer(data=registro)
            if serializer.is_valid():
                serializer.save()
                registros_exitosos.append(serializer.data)
            else:
                errores.append(serializer.errors)
        
        if errores:
            return JSONResponseErr({"errors": errores}, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOkRows(registros_exitosos, msg="Registros guardados con éxito")

    
class Detalle_BoletaDetail(APIView):
    def get_object(self, pk):
        try:
            return Detalle_Boleta.objects.get(pk=pk)
        except Detalle_Boleta.DoesNotExist:
            raise Http404
    
    # MOSTRAR UNO POR PK    
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = Detalle_BoletaSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    # ACTUALIZAR UNO POR PK
    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = Detalle_BoletaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ELIMINAR UNO POR PK
    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################################
#########################################################################

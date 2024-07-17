from django.contrib import admin
from django.urls import path, include
from ventas import views

urlpatterns = [
    path('moto/', views.MotoList.as_view()),
    path('moto/<int:pk>', views.MotoDetail.as_view()),
    path('moto/motoUpload/', views.MotoUpload.as_view()),  

    path('marca/', views.MarcaList.as_view()),
    path('marca/<int:pk>', views.MarcaDetail.as_view()),
    path('marca/marcaUpload/', views.MarcaUpload.as_view()), 

    path('tipomoto/', views.TipoMotoList.as_view()),
    path('tipomoto/<int:pk>', views.TipoMotoDetail.as_view()),
    path('tipomoto/tipomotoUpload/', views.TipoMotoUpload.as_view()), 

    path('cliente/', views.ClienteList.as_view()),
    path('cliente/<int:pk>', views.ClienteDetail.as_view()),
    path('cliente/clienteUpload/', views.ClienteUpload.as_view()), 

    path('empleado/', views.EmpleadoList.as_view()),
    path('empleado/<int:pk>', views.EmpleadoDetail.as_view()),
    path('empleado/empleadoUpload/', views.EmpleadoUpload.as_view()), 

    path('cargo/', views.CargoList.as_view()),
    path('cargo/<int:pk>', views.CargoDetail.as_view()),
    path('cargo/cargoUpload/', views.CargoUpload.as_view()), 

    path('boleta/', views.BoletaList.as_view()),
    path('boleta/<int:pk>', views.BoletaDetail.as_view()),
    path('boleta/boletaUpload/', views.BoletaUpload.as_view()), 

    path('detalleboleta/', views.Detalle_BoletaList.as_view()),
    path('detalleboleta/<int:pk>', views.Detalle_BoletaDetail.as_view()),
    path('detalleboleta/detalleboletaUpload/', views.Detalle_BoletaUpload.as_view()), 












    path('carritocompras/', views.Carrito_comrasList.as_view()),
    path('carritocompras/<int:pk>', views.Carrito_comprasDetail.as_view()),
    path('carritocompras/Carrito_comprasUpload/', views.Carrito_comprasUpload.as_view()), 

    
]
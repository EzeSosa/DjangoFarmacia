from django.contrib import admin
from appfarmacia.models import *

# Register your models here.

@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = (
        'idunidadmedida',
        'nombre',
        'descripcion',
    )
    ordering = ['idunidadmedida']
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = (
        'idlocalidad',
        'nombre',
    )
    ordering = ['idlocalidad']
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'idtipodocumento',
        'nombre',
    )
    ordering = ['idtipodocumento']
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = (
        'idtipoproducto',
        'nombre',
    )
    ordering = ['idtipoproducto']  
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        'iddireccion',
        'calle',
        'altura',
    )
    ordering = ['iddireccion'] 
    search_fields = ['calle']
    list_filter = (
        'iddireccion',
    )

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'idempleado',
        'nombre',
        'telefono',
    )
    ordering = ['idempleado']  
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'idproveedor',
        'nombre',
        'telefono',
    )
    ordering = ['idproveedor'] 
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'idproducto',
        'nombre',
        'dosis',
        'precio',
    )
    ordering = ['idproducto'] 
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'idventa',
        'fecha',
        'hora',
    )
    ordering = ['idventa'] 
    search_fields = ['idventa']
    list_filter = (
        'idventa',
    )

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'idproductoproveedor',
        'precio',
        'cantidad',
    )
    ordering = ['idproductoproveedor']  
    search_fields = ['idproductoproveedor']
    list_filter = (
        'idproductoproveedor',
    )

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = (
        'iddetalleventa',
        'cantidad',
        'preciounitario',
    )
    ordering = ['iddetalleventa']  
    search_fields = ['iddetalleventa']
    list_filter = (
        'iddetalleventa',
    )
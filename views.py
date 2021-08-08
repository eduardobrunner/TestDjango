from django.http import HttpResponse
import datetime
from django.template import Template, Context


def Saludo(request):#esta vista debe recibir un request como primer argumento. PRIMERA VISTA
    
    doc_externo = open("C:/Users/Eduardo/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantilla1.html")

    mi_plantilla = Template(doc_externo.read())

    doc_externo.close()

    contexto = Context()

    documento = mi_plantilla.render(contexto)
    
    return HttpResponse(documento) #nos devuelve un texto

def dameFecha(request):
    fecha_actual=datetime.datetime.now() 

    doc="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(doc)

def calculaEdad(request,edad,anio):
    periodo = anio - 2021
    edadFutura = edad+periodo
    doc = "<html><body><h2>En el año %s tendras %s años</h2></body></html>"%(anio,edadFutura)

    return HttpResponse(doc)
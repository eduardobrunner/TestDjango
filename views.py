from django.http import HttpResponse
import datetime

def Saludo(request):#esta vista debe recibir un request como primer argumento. PRIMERA VISTA
    return HttpResponse("Hola Mundo!!!") #nos devuelve un texto

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
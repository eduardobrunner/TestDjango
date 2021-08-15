from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader  #importar el cargador de plantillas
                                    #su metodo clave es loader.get_template

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre

        self.apellido = apellido

def Saludo(request):#esta vista debe recibir un request como primer argumento. PRIMERA VISTA
    
    p1=Persona("Romulo","Brunner")
    
    ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/Eduardo/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla1.html")

    mi_plantilla = Template(doc_externo.read())

    doc_externo.close()

    contexto = Context({"mi_nombre":p1.nombre,
                        "mi_apellido":p1.apellido,
                        "tiempo_actual":ahora,
                        "colores":[]}) #esta lista se puede crear aparte e invocar la variable aqui
    #Se puede acceder a valores en la plantilla desde el contexto mediante diccionarios

    documento = mi_plantilla.render(contexto)
    
    return HttpResponse(documento) #nos devuelve un texto

def importando_plantilla(request):#esta vista debe recibir un request como primer argumento. PRIMERA VISTA
    
    p2=Persona("Eduardo","Brunner")
    
    ahora = datetime.datetime.now()

    importando_mi_plantilla=loader.get_template('plantilla1.html')

    contexto = {"mi_nombre":p2.nombre,
                "mi_apellido":p2.apellido,
                "tiempo_actual":ahora,
                "colores":[1,2,3]
                } 

    documento = importando_mi_plantilla.render(contexto)
    
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
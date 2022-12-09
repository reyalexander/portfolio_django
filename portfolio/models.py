from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
'''
Creación de formulario con los siguientes campos:

Foto (que puede ser una URL)
Título del proyecto
Descripción del proyecto
Tags: HTML, CSS, PYTHON, etc
URL de github
Formulario con validación
Para poder crear un ítem (proyecto) el usuario debe estar logueado.
Guardar la IP de las personas que visitan el sitio. En caso no haya hecho despliegue con railway (que es opcional) puede usar ngrok para guardar las IPs de las visitas.
Para la parte visual utilizar algunos de estos temas gratuitos de bootstrap:
Temas gratis de Theme Wagon
Templates gratuitos de Bootstrap made.
Templates gratuitos de Start Bootstrap. Prohibido usar el tema Freelancer (está demasiado usado en muchos lados)
Cualquier otro template.
'''

class Portfolio(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, null=True) #(que puede ser una URL)
    title = models.CharField(max_length=50) # Project Title
    description = models.TextField(max_length=500) # Project Description
    tags = models.CharField(max_length=100) # HTML, CSS, PYTHON, etc
    url = models.CharField(max_length=200) # URL de github
    
    def __str__(self):
        return self.title + ' - ' + self.url
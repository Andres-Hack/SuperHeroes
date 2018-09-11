from django.template.loader import get_template
from django.core.mail import EmailMessage
from rest_framework.response import Response

def Estados(datos):
	if int(datos['temperatura']) > 21:
		EnviarCorreo('Alerta la temperatura subio mas de lo normal, se encuentra por encima de los 21°C que es la temperatura ambiente del lugar.<br><i style="color:red">Nota : </i> se le sugiere apersonarse al lugar para ver la razon de dicha causa.')
	if datos['corriente1'] == 'danger':
		EnviarCorreo('Alerta, uno de lso enchufes no esta funcinando correctamente en la sala de servidores.<br><i style="color:red">Nota : </i> se le sugiere apersonarse al lugar para ver la razon de dicha causa.')
	if int(datos['humo']) == 0:
		EnviarCorreo('Alerta, se detecto precencia de humo dentro de la sala de servidores.<br><i style="color:red">Nota : </i> se le sugiere apersonarse al lugar para ver la razon de dicha causa.')
	if datos['movimiento'] == 'success':
		EnviarCorreo('Alerta, se detecto movimiento en la sala de servidores.<br><i style="color:red">Nota : </i> se le sugiere apersonarse al lugar para ver la razon de dicha causa.')

def EnviarCorreo(contenido):
	mail_content = contenido
	mail = EmailMessage('Alerta!!!', mail_content, 'servidor@oopp.gob.bo', to=['andresmamanielt@gmail.com'])
	mail.content_subtype = 'html'
	mail.send()
	return Response('Ok')


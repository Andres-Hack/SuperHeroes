from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, GroupViewSet, UserView, SalaViewSet, SalaList, SalaDetalle, ReporteView, SalaEstadosViewSet,  SalaEstadoPorFecha, SensoresViewSet, SensoresPorFecha

"""
RUTAS DE API REST
"""
api_router = SimpleRouter(trailing_slash=True)
api_router.register(r'users', UserViewSet, base_name='usuarios')
api_router.register(r'groups', GroupViewSet, base_name='grupos')
api_router.register(r'sala', SalaViewSet, base_name='sala')
api_router.register(r'sala/(?P<user_pk>[0-9]+)/detalle', UserView, base_name='inscripcion')
api_router.register(r'sensores', SensoresViewSet, base_name='sensores_list')

"""
RUTAS DE LOS REPORTES
"""
report_router = SimpleRouter(trailing_slash=True)
report_router.register(r'estados', SalaEstadosViewSet, base_name='sala_es')
report_router.register(r'detalle/(?P<fecha>[0-9]{4}-[0-9]{2}-[0-9]{2})', SalaEstadoPorFecha, base_name='sala_detalle')
report_router.register(r'sensor/(?P<fecha_sensor>[0-9]{4}-[0-9]{2}-[0-9]{2})', SensoresPorFecha, base_name='sensores_detalle')

urlpatterns = [
    url(r'^', include(api_router.urls)),
    url(r'^reportes/', include(report_router.urls)),
    url(r'^api_sala/$', SalaList.as_view()),
    url(r'^api_sala/(?P<pk>[0-9]+)/$', SalaDetalle.as_view()),
    url(r'^api_reporte/(?P<pk>\d+)/$', ReporteView.as_view()),
]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .views import (inicio, crear_criatura, formulario_criatura, criaturas_usuario,
                    registro_usuario, formulario_registro_usuario)


urlpatterns = [
    path('', inicio, name='index'),
    path('crear_criatura/', login_required(crear_criatura), name='crear_criatura'),
    path('login/', LoginView.as_view(template_name='Dex/iniciar_sesion.html'), name='inicio_sesion'),
    path('logout/', LogoutView.as_view(template_name='Dex/ver_criaturas.html'), name='cerrar_sesion'),
    path('form_criatura/', login_required(formulario_criatura), name='formulario_criatura'),
    path('criaturas_usuario/', login_required(criaturas_usuario), name='criaturas_usuario'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('form_registro/', formulario_registro_usuario, name='formulario_registro_usuario'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django import urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    

    path ('', views.Socio, name="Socio"),
    path ('Listar_Socios', views.ListarSocios, name="listar_socios"),
    path ('Modificar_Socio/<id>/', views.ModificarSocio, name="modificar_socio"),
    path ('Registro_Usuario', views.RegistroUsuario, name="registro_usuario"),
    path ('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html"), name="reset_password"),
    path ('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path ('reset/<uidf64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path ('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('mensual', views.view_mensual, name='view_mensual'),
    path('create', views.create_maintenance, name='create_maintenance'),
    path('delete/<int:pk>', views.delete_maintenance, name='delete_maintenance'),
    path('form/<int:pk>', views.form_maintenance, name='form_maintenance'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cfs_dashboard, name='cfs_dashboard'),
    path('photographic', views.view_infFotografico, name='photographic_view'),
    path('photographic/create', views.create_infFotografico, name='photographic_create'),
    path('photographic/<int:pk>', views.photographic_view_one, name='photographic_view_one'),
    path('photographic/<int:pk>/evidence', views.photographic_create_row, name='photographic_create_row'),
    path('photographic/generate/<int:pk>', views.photographic_generate, name='photographic_generate'),
    path('photographic/delete/<int:pk>', views.photographic_delete, name='photographic_delete'),
    path('photographic/evidence/delete/<int:pk>', views.photographic_delete_item, name='photographic_delete_item'),
]
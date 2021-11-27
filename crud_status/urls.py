from django.urls import path
from .views import index_status, index_tambah_status, index_update_status, index_update_status

urlpatterns = [
    path('', index_status, name='index_status_tiket'),
    path('tambah-status-tiket/', index_tambah_status, name='index_tambah_status'),
    path('update-status-tiket/', index_update_status, name='index_update_status'),
]
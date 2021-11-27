from django.urls import path
from .views import index_instansi, index_tambah_instansi, index_update_instansi, index_detail_instansi

urlpatterns = [
    path('', index_instansi, name='index_instansi'),
    path('tambah-instansi/', index_tambah_instansi, name='index_tambah_instansi'),
    path('update-instansi/', index_update_instansi, name='index_update_instansi'),
    path('detail-instansi/', index_detail_instansi, name='index_detail_instansi'),
]
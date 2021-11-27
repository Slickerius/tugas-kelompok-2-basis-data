from django.urls import path
from .views import index, index_tiket_saya

urlpatterns = [
    path('', index, name='index_cr_tiket'),
    path('tiket-saya/', index_tiket_saya, name='index_tiket_saya'),
]
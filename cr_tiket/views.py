from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_cr_tiket.html', {})
    
def index_tiket_saya(request):
    return render(request, 'index_tiket_saya.html', {})
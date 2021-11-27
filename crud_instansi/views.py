from django.shortcuts import render

# Create your views here.
def index_instansi(request):
    return render(request, 'instansi.html', {})
    
def index_tambah_instansi(request):
    return render(request, 'tambah_instansi.html', {})

def index_update_instansi(request):
    return render(request, 'update_instansi.html', {})

def index_detail_instansi(request):
    return render(request, 'detail_instansi.html', {})
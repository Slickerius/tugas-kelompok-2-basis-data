from django.shortcuts import render

# Create your views here.
def index_status(request):
    return render(request, 'status_tiket.html', {})
    
def index_tambah_status(request):
    return render(request, 'tambah_status_tiket.html', {})

def index_update_status(request):
    return render(request, 'update_status_tiket.html', {})
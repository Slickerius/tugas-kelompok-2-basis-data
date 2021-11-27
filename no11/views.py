from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.core import serializers

def index(request):
    return render(request, 'index_no11.html', {})

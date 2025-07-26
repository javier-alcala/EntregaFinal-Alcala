from django.shortcuts import render

def inicio(request):
    return render(request, 'blog/inicio.html')

def sobreMi(request):
    return render(request, 'blog/sobre_mi.html')
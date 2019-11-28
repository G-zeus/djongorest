from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
 
from .models import Categoria
 
# Create your views here.


def categoria_list(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"results": list(cat.values("description","activo"))}
    return JsonResponse(data)


def categoria_detalle(request,pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {"results": {
        "description": cat.description,
        "activo": cat.activo
        }}
    return JsonResponse(data)

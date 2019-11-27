#from rest_framework.views import APIView
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework import generics
 
from .models import Producto
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer 
 
#class ProductoList(APIView):
#    def get(self,request):
#        prod = Producto.objects.all()[:20]
#        data = ProductoSerializer(prod, many=True).data
#        return Response(data)
 
#class ProductoDetalle(APIView):
#    def get(self,request,pk):
#        prod = get_object_or_404(Producto, pk=pk)
#        data = ProductoSerializer(prod).data
#        return Response(data)
 
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
 
 
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaSave(generics.CreateAPIView):
    serializer_class = CategoriaSerializer
 
class SubCategoriaSave(generics.CreateAPIView):
        serializer_class = SubCategoriaSerializer
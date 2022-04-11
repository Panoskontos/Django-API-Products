from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    products_serialized = ProductSerializer(products, many=True)
    return Response(products_serialized.data)

@api_view(['GET'])
def product(request, pk):
    product = Product.objects.get(id=pk)
    products_serialized = ProductSerializer(product, many=False)
    return Response(products_serialized.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(data=request.data, instance=product)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Product was deleted!')
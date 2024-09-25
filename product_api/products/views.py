from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


def index(request):
    """Отображает HTML-страницу с интерфейсом для взаимодействия с API."""
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def product_list_create(request):
    """Обрабатывает GET и POST-запросы для работы с продуктами."""
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import pytest
from django.urls import reverse
from products.models import Product
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_product_invalid_price(api_client):
    url = reverse('product-list-create')
    data = {
        'name': 'Test Product',
        'description': 'Test Product.',
        'price': '-5.00'
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'price' in response.data
    assert response.data['price'][0] == "Цена должна быть больше нуля."


@pytest.mark.django_db
def test_create_product(api_client):
    url = reverse('product-list-create')
    data = {
        'name': 'Test Product',
        'description': 'Test Product.',
        'price': '12.99'
    }

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 1
    assert Product.objects.get().name == 'Test Product'


@pytest.mark.django_db
def test_get_product_list(api_client):
    Product.objects.create(
        name='Product1',
        description='Description1',
        price=10.50
    )
    Product.objects.create(
        name='Product2',
        description='Description2',
        price=15.00
    )

    url = reverse('product-list-create')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == 'Product1'
    assert response.data[1]['name'] == 'Product2'

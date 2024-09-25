from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product."""

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        """Проверяем, что цена продукта больше нуля."""
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля.")
        return value

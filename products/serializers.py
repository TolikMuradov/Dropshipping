from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price_local(self, value):
        if value <= 0:
            raise serializers.ValidationError("Satış fiyatı 0'dan büyük olmalı.")
        return value

    def validate_price_cny(self, value):
        if value <= 0:
            raise serializers.ValidationError("Alış fiyatı 0'dan büyük olmalı.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stok negatif olamaz.")
        return value
from account.models import Products
from rest_framework import serializers

class Productser(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
from rest_framework import serializers
from django.db.models import fields
from main.models import Account


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
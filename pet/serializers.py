# from rest_framework import serializers
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'email', 'wallet_balance']

# class SendMoneySerializer(serializers.Serializer):
#     receiver_id = serializers.IntegerField()
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2)

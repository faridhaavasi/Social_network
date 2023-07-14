from rest_framework import serializers
from account.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'password is not match'})
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'], email=validated_data['email'],
            password=validated_data['password']
        )


# API/serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'fecha_nacimiento', 'telefono_contacto', 'nombre_cliente']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            fecha_nacimiento=validated_data.get('fecha_nacimiento'),
            telefono_contacto=validated_data.get('telefono_contacto'),
            nombre_cliente=validated_data.get('nombre_cliente', '')
        )
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.fecha_nacimiento = validated_data.get('fecha_nacimiento', instance.fecha_nacimiento)
        instance.telefono_contacto = validated_data.get('telefono_contacto', instance.telefono_contacto)
        instance.nombre_cliente = validated_data.get('nombre_cliente', instance.nombre_cliente)

        # Solo actualizar la contraseña si se proporciona una nueva
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate_username(self, value):
        request = self.context.get('request')
        if request and request.method in ['PUT', 'PATCH']:
            user_id = request.parser_context['kwargs']['pk']
            if CustomUser.objects.filter(username=value).exclude(id=user_id).exists():
                raise serializers.ValidationError("Este nombre de usuario ya existe. Ingresa un nuevo nombre de usuario.")
        return value

    def validate_email(self, value):
        request = self.context.get('request')
        if request and request.method in ['PUT', 'PATCH']:
            user_id = request.parser_context['kwargs']['pk']
            if CustomUser.objects.filter(email=value).exclude(id=user_id).exists():
                raise serializers.ValidationError("Este correo electrónico ya está registrado. Ingresa un nuevo correo electrónico.")
        return value

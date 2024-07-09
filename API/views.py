# API/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib.auth import authenticate
from .serializers import UserSerializer


@api_view(['POST'])
def crear_usuarios(request):
    if isinstance(request.data, list):
        usuarios = request.data
        resultado = []
        for usuario in usuarios:
            serializer = UserSerializer(data=usuario)
            if serializer.is_valid():
                serializer.save()
                resultado.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(resultado, status=status.HTTP_201_CREATED)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def actualizar_usuario(request, usuario_id):
    try:
        usuario = CustomUser.objects.get(pk=usuario_id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(usuario, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = CustomUser.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def eliminar_usuario(request, pk):
    try:
        usuario = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        usuario.delete()
        return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def autenticar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({"message": "Usuario autenticado"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Usuario o contraseña inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def obtener_usuario_por_username(request, username):
    try:
        usuario = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(usuario)
    return Response(serializer.data, status=status.HTTP_200_OK)
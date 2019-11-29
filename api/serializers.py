from rest_framework import serializers, generics
from rest_framework.authtoken.models import Token
from .models import Producto, Categoria, SubCategoria
from django.contrib.auth.models import User


class ProductoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Producto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = '__all__'


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubCategoriaList(generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer

# Los métodos de la clase ProductoSerializer

# La clase ProductoSerializer construida en la clase anterior, tiene varios métodos:

# is_valid(self, ...): Dice si la data es suficiente y válida
#  para crear/actualizar una instancia modelo.

# save(self, ...): El cual sabe cómo crear o actualizar un modelo.

# create(self, validated_data, ..): Sabe cómo crear la instancia.
#  Se puede sobreescribir para poder personalizar la tarea de creación.

# update(self, instance, validated_data, ..): Sabe cómo actualizar la instancia.
#  Se puede sobreescribir para poder personalizar la tarea de actualización.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

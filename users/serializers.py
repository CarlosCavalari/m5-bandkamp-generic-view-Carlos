from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
    )
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        return User.objects.create_superuser(**validated_data)
    
    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value) 
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser"
        ]
    

    # id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(
    #     validators=[
    #         UniqueValidator(
    #             queryset=User.objects.all(),
    #             message="A user with that username already exists.",
    #         )
    #     ],
    # )
    # email = serializers.EmailField(
    #     validators=[UniqueValidator(queryset=User.objects.all())],
    # )
    # password = serializers.CharField(write_only=True)
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)
    # is_superuser = serializers.BooleanField(read_only=True)

    # def create(self, validated_data: dict) -> User:
    #     return User.objects.create_superuser(**validated_data)

    # def update(self, instance: User, validated_data: dict) -> User:
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #         if key == "password":
    #             instance.set_password(value)
    #     instance.save()

    #     return instance

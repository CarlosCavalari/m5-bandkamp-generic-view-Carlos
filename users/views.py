from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework import generics

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer: User):
        serializer.save()
        return

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"
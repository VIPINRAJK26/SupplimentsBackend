from supplimentApp.permissions import IsLoggedIn
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from supplimentApp.models import *
from supplimentApp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.


class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = UserType.objects.get(
                    name=username,
                    password=password
                )

                return Response({
                    "success": True,
                    "message": "Login Successful",
                    "user": {
                        "id": user.id,
                        "name": user.name
                    }
                })

            except UserType.DoesNotExist:

                return Response({
                    "success": False,
                    "message": "Invalid credentials"
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors)

class UserTypeView(ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrdersView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    # permission_classes = [IsLoggedIn]

from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]




# class ProductListAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         objects = Product.objects.all()
#         serializer = ProductSerializer(objects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)




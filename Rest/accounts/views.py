from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)   #به  عنوان دیتا ارسال میشه چون از طریق کاربر میاد و باید اعتبار سنجی بشه برخلاف هوم که اینستنس ارسال شد چون اطلاعات را از دیتابیس میخوانیم
        if ser_data.is_valid():
            # User.objects.create_user( #ثبت نام کاربر
            #     username=ser_data.validated_data['username'],
            #     email=ser_data.validated_data['email'],
            #     password=ser_data.validated_data['password'],
            # )
            ser_data.create(ser_data.validated_data)#از سریالایزر میگیره پس بالا را نمیخاد
            return Response(ser_data.data, status=status.HTTP_201_CREATED)  # اگه اطلاعات تایید شده بود این را برمیگرداند
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST) #اگه اطلاعات تایید شده نبود ارور برمیگرداند


# برای کدهای کوتاه بهتر است از ViewSetاستفاده بشه  و  برای کد های طولانی از  APIView استفاده شود

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserSerializer(instance=user)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'you are not the owner'})
        srz_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'permission denied': 'you are not the owner'})
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated'})













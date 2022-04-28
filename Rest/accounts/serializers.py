from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):  # چندتا ولیدیشن روی یک فیلد باشه
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')


# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)  # required=True اجباری بودن این فیلد با
#     email = serializers.EmailField(required=True, validators=[clean_email])
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

    # def validate_username(self, value):  # فقط یه فیلد را اتبار سنجی میکنه
    #     if value == 'admin':
    #         raise serializers.ValidationError('username cant be `admin` ')
    #     return value

    # def validate(self, data):  # کل داده ای که از سمت کاربر میاد
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError('password must match')
    #     return data


#modelserializer

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True) #یک فیلدی که داخل مدل نیست را اضافه میکنیم

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        #fields = '__all__'  #همه فیلدها
        # fields = ('username')یکی یا دوتا از فیلدها
        # excludes = ('username')همه بجز اینکه داخل پرانتزه
        extra_kwargs = {#اضافه کردن یک ویژگی به فیلدها
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be `admin`')
        return value

    def validate(self, data):  # کل داده ای که از سمت کاربر میاد
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
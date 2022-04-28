from django.urls import path
from . import views
#from rest_framework.authtoken import views as auth_tokenچون دیگه از اتنتیکیشن جنگو استفاده نمیکنبم و از جی وی اتنتیکیشن استفاده میکنیم
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    # path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#ایجاد کردن یک توکن
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#رفرش توکن های منقضی

]


router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls


#{
#  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MDY0ODg1OCwiaWF0IjoxNjUwNTYyNDU4LCJqdGkiOiJmMzk0YmEyNThhNWE0ZWJiYjcxYjRlMGJmZmFmY2JjNCIsInVzZXJfaWQiOjF9.JlP1n5RZI_BrzT01QceNvho73-1mE9spFVM5szWY-lM",
# "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwNTYyNzU4LCJpYXQiOjE2NTA1NjI0NTgsImp0aSI6IjNjMmRmNTJiZDMxZTRiNTY5YjliMjk2MDc3NzU0MWFhIiwidXNlcl9pZCI6MX0.2AyRxqO14fHSIsxIk5V1xy32EwlCuesbKO1eoh1AxGg"
#}
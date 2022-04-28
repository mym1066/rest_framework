# from rest_framework.decorators import api_view #Function Based Views
from rest_framework.views import APIView  # Class-based Views
from rest_framework.response import Response
from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly

# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Create your views here.


# Function Based Views
# اجباری است @api_view
# @api_view(['GET','POST','PUTE'])# اگه پرانتز خالی باشه یعنی با گت بیاو میتوانیم بگ.ییم با چه متدهایی ارسال بشه
# def home(request):
#   return Response({'name':'mrym'})

# Class-based Views

class Home(APIView):
    permission_classes = [IsAuthenticated,]
    # permission_classes = [IsAdminUser,]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)  # چون چندتا اطلاعات و داده به سریالایزر ارسال میشه و اگه یکی بود احتیاجی به منی نداشت
        return Response(data=ser_data.data)

    # def post(self, request):#چون از مدل سریالایزر در فایل سریالایزر استفاده نکردیم باید تک تک اضافه کنیم
    #   name = request.data['name']
    #    return Response({'name': name})


class QuestionListView(APIView):
    # throttle_classes = UserRateThrottle, AnonRateThrottle
    throttle_scope = 'questions'

    def get(self, request):  # اطلاعات را بخواند
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        create a new question
    """
    permission_classes = [IsAuthenticated, ]  # قبل از اینکه کاربر چیزی را اضافه کنه حتما اتنتیکیشن شود با استفاده از توکن ها
    serializer_class = QuestionSerializer

    def post(self, request):  # اطلاعات را ایجاد کنه
        srz_data = QuestionSerializer(data=request.data)  # اطلاعاتی که از سمت کاربر می اید
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):  # اپدیت کنه
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data,
                                      partial=True)  # پارشیال یعنی شاید اطلاعات نقص بیاد و قبول کن
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):  # حذف کنه
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'massage': 'question delete'}, status=status.HTTP_200_OK)

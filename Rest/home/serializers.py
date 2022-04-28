from rest_framework import serializers
from .models import Question, Answer
from .custom_relational_fields import UserEmailNameRelationalField

class PersonSerializer(serializers.Serializer):  # معادل فیلدهای مدل را داخل سریالایزر مینویسیم
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()



class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()  # اینSerializerMethodField یک فیلد را به یک متد خاص وصل میکنه
    user = UserEmailNameRelationalField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        result = obj.answers.all()  # تمام پاسخ های مربوط به این سوال
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

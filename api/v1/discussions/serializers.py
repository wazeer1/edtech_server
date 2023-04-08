from rest_framework import serializers
from discussions.models import *
from accounts.models import *


class QuestionSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    answer_count = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'user_details',
            'answer_count'
        )

    def get_user_details(self, instance):
        if instance.user.photo:
            photo = instance.user.photo
        else:
            photo = ''
        user_details = {
            "name":instance.user.name,
            "photo":photo
        }
        return user_details
    
    def get_answer_count(self, instance):
        question = Question.objects.get(question=instance, is_deleted=False)
        answer_count = Answer.objects.filter(question=question, is_deleted=False).count()
        return answer_count
    

class AddQuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    topic = serializers.CharField()
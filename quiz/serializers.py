from rest_framework import serializers
from .models import Quizzes, Question, UserSubmittedAnswer, Category
from account.models import UserProfile


class QuizzesSerializer(serializers.ModelSerializer):
    difficulty_level = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    class Meta:
        model = Quizzes
        fields = [
            'title',
            # 'questions',


        ]

    def get_questions(self, instance):
        questions = Question.objects.filter(quiz__id=instance.id).values(
            # 'title',
            # 'opt_1',
            # 'opt_2',
            # 'opt_3',
            # 'opt_4',
            # 'difficulty_level',
            # 'right_opt',
            # 'score',

        )
        return questions

    def get_difficulty_level(self, instance):
       difficulty_level = Question.objects.filter(difficulty_level=instance.id).values(
            'title',
            'opt_1',
            'opt_2',
            'opt_3',
            'opt_4',
            'difficulty_level',
            'right_opt',
            'score',
        )
       return difficulty_level


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'difficulty_level',
            'opt_1',
            'opt_2',
            'opt_3',
            'opt_4',
            'right_opt',
            'score',

        ]


class UserSubmittedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmittedAnswer
        fields = [
            'user_fk',
            'score'

        ]
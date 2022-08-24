from django.contrib import admin

import account
from account import models
from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    category = models.Quizzes.title
    fields = [
        'title',
        'quiz',
        'difficulty_level',
        'opt_1',
        'opt_2',
        'opt_3',
        'opt_4',
        'right_opt',
        'score'
    ]
    list_display = [
        'title',
        'quiz',
        'difficulty_level',
        'opt_1',
        'opt_2',
        'opt_3',
        'opt_4',
        'right_opt',
        'score'
    ]


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    user_kf = account.models.UserProfile

    list_display = (
        'user_kf',
        'score'
    )


admin.site.register(models.UserSubmittedAnswer, UserSubmittedAnswerAdmin)

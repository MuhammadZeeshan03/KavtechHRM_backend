from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    objects = None

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    Difficulty_level = (

        (0, _('Fresher')),
        (1, _('Intermediate')),
        (2, _('Advanced')),
        (3, _('Expert'))
    )

    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty_level = models.IntegerField(
        choices=Difficulty_level, default=0, verbose_name=_("Difficulty level"))
    opt_1 = models.CharField( max_length=255, verbose_name=_("Option 1"))
    opt_2 = models.CharField( max_length=255, verbose_name=_("Option 2"))
    opt_3 = models.CharField( max_length=255, verbose_name=_("Option 3"))
    opt_4 = models.CharField( max_length=255, verbose_name=_("Option 4"))
    right_opt = models.CharField(max_length=100,  verbose_name=_("Right option"))
    score = models.IntegerField(null=False, default=0)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    def __str__(self):
        return self.title


#
class UserSubmittedAnswer(models.Model):
    user_fk = models.OneToOneField('account.UserProfile',
                                verbose_name=_("User Profile"), on_delete=models.CASCADE, unique=True)
    score = models.IntegerField(default=0)
    def __int__(self):
        return self.user_fk





from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Questionnaire(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('radio', 'Radio'),
        ('input', 'Input'),
        ('textarea', 'Textarea')
    ]

    section = models.ForeignKey(Section, to_field='title', related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    options = models.JSONField(blank=True, null=True)  # Only used if question_type is 'radio'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Response(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='responses', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.questionnaire.title}"

class Answer(models.Model):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)  # For input and textarea
    answer_choice = models.CharField(max_length=255, blank=True, null=True)  # For radio
    question_type = models.CharField(max_length=10, choices=Question.QUESTION_TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.response} - {self.question.text}"


from rest_framework import serializers
from .models import Questionnaire, Section, Question, Response, Answer

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, data):
        question = data.get('question')
        if question.question_type == 'radio' and not data.get('answer_choice'):
            raise serializers.ValidationError("Answer choice is required for radio questions.")
        if question.question_type in ['input', 'textarea'] and not data.get('answer_text'):
            raise serializers.ValidationError("Answer text is required for input/textarea questions.")
        return data

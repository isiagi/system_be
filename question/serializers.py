from rest_framework import serializers
from .models import Questionnaire, Section, Question, Response, Answer, Subsection, Subsubsection

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'

# class SectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Section
#         fields = '__all__'
#         depth = 2

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SubsubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsubsection
        fields = ['id', 'title', 'subsection', 'description']



class SubsectionSerializer(serializers.ModelSerializer):
    subsubsections = SubsubsectionSerializer(many=True, read_only=True)
    class Meta:
        model = Subsection
        fields = ['id', 'title', 'section', 'description', 'subsubsections']

# class SubsectionSerializer(serializers.ModelSerializer):
#     subsubsections = SubsubsectionSerializer(many=True, read_only=True)  # Corrected field name

#     class Meta:
#         model = Subsection
#         fields = ['id', 'title', 'section', 'description', 'subsubsections']  # Corrected field name



class SectionSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer(many=True, read_only=True)
    # subsection_questions = QuestionSerializer(many=True, read_only=True)
    # subsections = serializers.SerializerMethodField()
    subsections = SubsectionSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'description', 'subsections']


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        depth = 2

    # def validate(self, data):
    #     # Validate the answer choice if the question type is radio
    #     print(data,'datagggg')
    #     question = data.get('question_type')
    #     if question == 'radio' and not data.get('answer_choice'):
    #         raise serializers.ValidationError("Answer choice is required for radio questions.")
    #     if question in ['input', 'textarea'] and not data.get('answer_text'):
    #         raise serializers.ValidationError("Answer text is required for input/textarea questions.")
    #     return data

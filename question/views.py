from rest_framework import viewsets
from .models import Questionnaire, Section, Question, Response, Answer
from .serializers import QuestionnaireSerializer, SectionSerializer, QuestionSerializer, ResponseSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [IsAuthenticated]

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(response=self.get_response())

    def get_response(self):
        # Retrieve the response related to the current user and questionnaire
        response_id = self.request.data.get('response_id')
        return Response.objects.get(id=response_id, user=self.request.user)

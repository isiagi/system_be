from rest_framework import viewsets
from .models import Questionnaire, Section, Question, Response, Answer
from .serializers import QuestionnaireSerializer, SectionSerializer, QuestionSerializer, ResponseSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    # Get questions for a specific section
    def get_queryset(self):
        section_id = self.kwargs.get('section_id')
        # if section_id is not present return all questions
        if section_id is None:
            return Question.objects.all()
        return Question.objects.filter(section=section_id)

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    # user = self.request.user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import status
from rest_framework.response import Response as DRFResponse

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Expecting `request.data` to be a list of answers
        answers_data = request.data
        print(answers_data,'answers_data')
        if not isinstance(answers_data, list):
            return DRFResponse({"detail": "Invalid data format. Expected a list of answers."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the response related to the current user and questionnaire
        response_instance = self.get_response()
        
        # Collect all the created answers
        created_answers = []
        
        for answer_data in answers_data:
            serializer = self.get_serializer(data=answer_data)
            if serializer.is_valid():
                serializer.save(response=response_instance,question_id=answer_data.get('question'))
                created_answers.append(serializer.data)
            else:
                return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return DRFResponse(created_answers, status=status.HTTP_201_CREATED)

    def get_response(self):
        # Retrieve the response related to the current user and questionnaire
        response_id = self.request.data[0].get('response')  # Assuming request.data is a list
        return Response.objects.get(id=response_id, user=self.request.user)


# class AnswerViewSet(viewsets.ModelViewSet):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     # permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(response=self.get_response())

#     def get_response(self):
#         # Retrieve the response related to the current user and questionnaire
#         response_id = self.request.data.get('response')
#         return Response.objects.get(id=response_id, user=self.request.user)



# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action

# class AnswerViewSet(viewsets.ModelViewSet):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     # permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(response=self.get_response())

#     def get_response(self):
#         # Retrieve the response related to the current user and questionnaire
#         response_id = self.request.data.get('response')
#         return Response.objects.get(id=response_id, user=self.request.user)

#     def create(self, request, *args, **kwargs):
#         # Handle the case where multiple answers are sent in the request body
#         answers_data = request.data
#         response_id = self.get_response().id
        
#         if not isinstance(answers_data, list):
#             return Response({"detail": "Invalid data format, expected an array of answers."}, status=status.HTTP_400_BAD_REQUEST)

#         # Iterate through the answers and create each one
#         for answer_data in answers_data:
#             answer_data['response'] = response_id
#             serializer = self.get_serializer(data=answer_data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
        
#         headers = self.get_success_headers(answers_data)
#         return Response(answers_data, status=status.HTTP_201_CREATED, headers=headers)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionnaireViewSet, SectionViewSet, QuestionViewSet, ResponseViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'questionnaires', QuestionnaireViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sections/<str:section_id>/questions/', QuestionViewSet.as_view({'get': 'list'}), name='section-questions'),
    path('<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve'}), name='question-detail'),
    # delete question
    path('<int:pk>/delete/', QuestionViewSet.as_view({'delete': 'destroy'}), name='question-delete'),
]

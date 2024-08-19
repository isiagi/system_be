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
    path('sections/<str:section_id>/questions/', QuestionViewSet.as_view({'get': 'list'}), name='section-questions')
]

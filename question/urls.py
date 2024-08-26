from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionnaireViewSet, SectionViewSet, QuestionViewSet, ResponseViewSet, AnswerViewSet, SubsectionViewSet, SubsubsectionViewSet, GroupedAnswerListView

router = DefaultRouter()
router.register(r'questionnaires', QuestionnaireViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'subsections', SubsectionViewSet, basename='subsections')
router.register(r'subsubsections', SubsubsectionViewSet, basename='subsubsections')
router.register(r'grouped-answers', GroupedAnswerListView, basename='grouped-answers')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:section_name>/<str:section_id>/questions/', QuestionViewSet.as_view({'get': 'list'}), name='section-questions'),
    path('<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve'}), name='question-detail'),
    # delete question
    path('<int:pk>/delete/', QuestionViewSet.as_view({'delete': 'destroy'}), name='question-delete'),
    # path('', SubsectionViewSet.as_view({'delete': 'destroy'}), name='questio'),
]

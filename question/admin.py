from django.contrib import admin
from question.models import Question, Answer, Response, Questionnaire, Section, Subsection, Subsubsection

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response)
admin.site.register(Questionnaire)
admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Subsubsection)

from django.contrib import admin

from backend.models import Keyword, Question, Answer, Vote, Attachment, Expert


admin.site.register(Keyword)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)
admin.site.register(Attachment)
admin.site.register(Expert)

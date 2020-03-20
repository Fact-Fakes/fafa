from rest_framework import viewsets
from backend.serializers import AllQuestionsSerializer
from backend.models import Question
from django.db.models import Q


class QuestionsViewsSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = AllQuestionsSerializer

    def get_serializer_context(self):
        sessionID = self.request.query_params.get("sessionID", None)
        if sessionID:
            return {"sessionID": sessionID}
        return {}

    def get_queryset(self):
        search = self.request.query_params.get("search", None)
        if search:
            return Question.objects.filter(
                Q(title__icontains=search) | Q(keywords__name__icontains=search)
            ).distinct()
        return super().get_queryset()

from rest_framework import viewsets
from rest_framework.response import Response
from backend.serializers import AllQuestionsSerializer
from backend.models import Question
from django.db.models import Q


class QuestionsViewsSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = AllQuestionsSerializer

    def get_serializer_context(self):
        sessionID = self.request.query_params.get("sessionID", None)
        action = self.action
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

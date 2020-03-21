from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins
from backend.serializers import (
    AllQuestionsSerializer,
    AnswerSerializer,
    VoteSerializer,
)
from backend.models import Question, Answer, Vote
from django.db.models import Q


class QuestionsViewsSet(viewsets.ModelViewSet):
    """ 
    View for getting all the questions or just one question based on pk  
    Params:
        sessionID (string) -> ID to identify user (use as required)
        search (string) -> String to search in titles and keywords
        page (int) -> Number of page to display

    """

    queryset = Question.objects.all()
    serializer_class = AllQuestionsSerializer
    http_method_names = ("get",)

    def get_serializer_context(self):
        """Method for getting sessionID from get parameter and passing it to AllQuestionSerializer"""
        sessionID = self.request.query_params.get("sessionID", None)
        action = self.action
        if sessionID:
            return {"sessionID": sessionID}
        return {}

    def get_queryset(self):
        """Method for change queryset based on search params"""
        search = self.request.query_params.get("search", None)
        if search:
            return Question.objects.filter(
                Q(title__icontains=search) | Q(keywords__name__icontains=search)
            ).distinct()
        return super().get_queryset()

    def retrieve(self, request, *args, **kwargs):
        """Method to retrieve one single object based on PK"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddAnswerViewSet(viewsets.ModelViewSet):
    """View for adding Answer"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ("post",)


class AddVoteViewSet(viewsets.ModelViewSet):
    """View for adding Vote"""

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    http_method_names = ("post",)

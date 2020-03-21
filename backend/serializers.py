from backend.models import Question, Answer, Keyword, Attachment, Vote
from rest_framework import serializers


class AttachmentSerializer(serializers.ModelSerializer):
    """Serializer for Attachment model. Used only in Questions endpoint and AllQuestionsSerializer"""

    class Meta:
        model = Attachment
        fields = ("pk", "name", "file")


class VoteSerializer(serializers.ModelSerializer):
    """Serializer for Vote model. Used only in AddVote view."""

    class Meta:
        model = Vote
        fields = ("question", "sessionID", "updown")


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for Answer model. Used only in AddAnswer view."""

    class Meta:
        model = Answer
        fields = ("question", "sessionID", "users_answer")


class AllQuestionsSerializer(serializers.ModelSerializer):
    """Serializer for Question model with ForeignKey and ManyToMany relationships. Used only in Questions view."""

    answers = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    def get_answers(self, obj):
        """ Method for quering answers based on sessionID """
        if sessionID := self.context.get("sessionID"):
            answers = Answer.objects.filter(question=obj, sessionID=sessionID).first()
            try:
                return answers.users_answer
            except AttributeError:
                return None
        return None

    def get_votes(self, obj):
        """ Method for quering votes based on sessionID """
        if sessionID := self.context.get("sessionID"):
            votes = Vote.objects.filter(question=obj, sessionID=sessionID).first()
            try:
                return votes.updown
            except AttributeError:
                return None
        return None

    def get_attachments(self, obj):
        """ Method for attachments  based on question """
        attachments = Attachment.objects.filter(question=obj)
        serializer = AttachmentSerializer(attachments, many=True)
        return serializer.data

    def get_keywords(self, obj):
        """ Method for quering keywords based on question """
        keywords = Keyword.objects.filter(questions=obj).values_list("name", flat=True)
        return keywords

    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "is_true",
            "real_answer",
            "yes_answers",
            "no_answers",
            "up_votes",
            "down_votes",
            "keywords",
            "answers",
            "votes",
            "attachments",
        )

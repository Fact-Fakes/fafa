from backend.models import Question, Answer, Keyword, Attachment, Vote, Expert
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


class ExpertSerializer(serializers.ModelSerializer):
    """Serializer for Expert model. Used only in AllQuestionsSerializer"""

    class Meta:
        model = Expert
        fields = ("name", "file", "website")


class AllQuestionsSerializer(serializers.ModelSerializer):
    """Serializer for Question model with ForeignKey and ManyToMany relationships. Used only in Questions view."""

    answers = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()
    experts = serializers.SerializerMethodField()

    def get_answers(self, obj):
        """ Method for quering answers based on sessionID """
        if sessionID := self.context.get("sessionID"):
            answers = obj.answer_set.filter(sessionID=sessionID).first()
            try:
                return answers.users_answer
            except AttributeError:
                return None
        return None

    def get_votes(self, obj):
        """ Method for quering votes based on sessionID """
        if sessionID := self.context.get("sessionID"):
            votes = obj.vote_set.filter(sessionID=sessionID).first()
            try:
                return votes.updown
            except AttributeError:
                return None
        return None

    def get_attachments(self, obj):
        """ Method for attachments  based on question """
        attachments = obj.attachment_set.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return serializer.data

    def get_keywords(self, obj):
        """ Method for quering keywords based on question """
        keywords = obj.keywords.all().values_list("name", flat=True)
        return keywords

    def get_experts(self, obj):
        """ Method for getting experts based on question """
        experts = obj.experts.all()
        serializer = ExpertSerializer(experts, many=True)
        return serializer.data

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
            "experts",
        )

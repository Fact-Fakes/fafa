from backend.models import Question, Answer, Keyword, Attachment, Vote
from rest_framework import serializers


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ("pk", "name", "file")


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("pk", "updown")


class AllQuestionsSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    def get_answers(self, obj):
        if sessionID := self.context.get("sessionID"):
            answers = Answer.objects.filter(question=obj, sessionID=sessionID).first()
            try:
                return answers.users_answer
            except AttributeError:
                return None
        return None

    def get_votes(self, obj):
        if sessionID := self.context.get("sessionID"):
            votes = Vote.objects.filter(question=obj, sessionID=sessionID)
            serializer = VoteSerializer(votes, many=True)
            return serializer.data
        return []

    def get_attachments(self, obj):
        attachments = Attachment.objects.filter(question=obj)
        serializer = AttachmentSerializer(attachments, many=True)
        return serializer.data

    def get_keywords(self, obj):
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

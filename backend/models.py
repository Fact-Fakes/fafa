from django.db import models
from django.db import transaction
from django.db.utils import IntegrityError


class Keyword(models.Model):
    """Keywords to identify a question topic"""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Expert(models.Model):
    """Experts for questions"""

    name = models.CharField(max_length=250, unique=True)
    file = models.FileField(upload_to="experts/")
    website = models.URLField(blank=True)


class Question(models.Model):
    """Single question with basic attributes"""

    title = models.CharField(max_length=255, unique=True)
    is_true = models.BooleanField(default=None)
    real_answer = models.TextField()
    yes_answers = models.IntegerField(default=0)
    no_answers = models.IntegerField(default=0)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    keywords = models.ManyToManyField(Keyword, related_name="questions", blank=True)
    experts = models.ManyToManyField(Expert, related_name="questions", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)


class Answer(models.Model):
    """User's single quiz answer"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sessionID = models.CharField(max_length=255)
    users_answer = models.BooleanField(default=None)

    class Meta:
        unique_together = ["sessionID", "question"]

    def save(self, *args, **kwargs):
        """A new answer updates counter in question model"""
        with transaction.atomic():
            if self.users_answer:
                self.question.yes_answers += 1
            else:
                self.question.no_answers += 1
            self.question.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question}: {self.users_answer}"


class Vote(models.Model):
    """User's single vote for a question"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sessionID = models.CharField(max_length=255)
    updown = models.BooleanField(default=None)

    class Meta:
        unique_together = ["sessionID", "question"]

    def save(self, *args, **kwargs):
        """A new vote updates counter in question model"""
        with transaction.atomic():
            if self.updown:
                self.question.up_votes += 1
            else:
                self.question.down_votes += 1
            self.question.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question}: {self.updown}"


class Attachment(models.Model):
    """Attachments for questions"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField()

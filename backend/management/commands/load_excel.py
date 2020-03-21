import openpyxl
import os

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.conf import settings
from backend.models import Question, Keyword, Expert

EXPERTS_FILES = {
    "dr Tomasz Rożek": "dr_tomasz_rozek.jpg",
    "Łukasz Sakowski": "lukasz_sakowski.jpg",
}

EXPERTS_WEBSITES = {
    "dr Tomasz Rożek": "http://www.naukatolubie.pl/",
    "Łukasz Sakowski": "https://www.totylkoteoria.pl/",
}


class Command(BaseCommand):  # pragma: no cover
    help = "Load excel document to database"
    row_items = (
        "expert",
        "question",
        "keywords",
        "is_true",
        "real_answer",
        "sources",
        "sources2",
        "sources3",
    )

    def add_arguments(self, parser):
        parser.add_argument("file", nargs="?", type=str, default="questions.xlsx")

    def handle(self, *args, **options):
        excel = openpyxl.load_workbook(options.get("file"))
        excel_obj = excel.active
        generated_data = [*self.generate_data(excel_obj)]
        question_objects = [*self.generate_question_objects(generated_data)]
        keyword_objects = [*self.generate_keywords_objects(generated_data)]
        experts_objects = [*self.generate_expert_objects(generated_data)]
        self.save_to_database(Question, question_objects)
        self.save_to_database(Keyword, keyword_objects)
        self.save_expert_to_database(experts_objects)
        self.add_keywords_to_questions(generated_data)
        self.add_experts_to_questions(generated_data)
        self.stdout.write(
            f"{len(question_objects)} questions and {len(keyword_objects)} keywords saved to database"
        )

    def generate_data(self, excel_obj: object):
        for row in excel_obj.iter_rows(min_row=2, min_col=1):
            temp_data = {}
            for i, cell in enumerate(row):
                if i == 1:
                    continue
                try:
                    temp_data.setdefault(
                        self.row_items[i if i < 1 else i - 1], cell.value
                    )
                except IndexError:
                    continue
            yield temp_data

    def generate_question_objects(self, data: list) -> Question:
        for item in data:
            if (
                item.get("question")
                and item.get("is_true") in [0, 1]
                and item.get("real_answer")
            ):
                answer = item["real_answer"]
                for i in range(3):
                    source = f"sources{i+1 if i != 0 else ''}"
                    answer += f" {item[source]}" if item[source] else ""
                yield Question(
                    title=item["question"], is_true=item["is_true"], real_answer=answer
                )

    def generate_keywords_objects(self, data: list) -> Keyword:
        keywords_temp = []
        for item in data:
            if keys := item.get("keywords"):
                keywords_temp.extend(keys.replace(" ", "").split(","))
        keywords = set(keywords_temp)
        for item in keywords:
            yield Keyword(name=item)

    def generate_expert_objects(self, data: list) -> Expert:
        experts_temp = []
        for item in data:
            if key := item.get("expert"):
                experts_temp.append(key)
        experts_temp = set(experts_temp)
        for item in experts_temp:
            yield Expert(name=item, website=EXPERTS_WEBSITES.get(item, None))

    def add_keywords_to_questions(self, data):
        questions = Question.objects.all()
        for question in questions:
            for key in data:
                if key.get("question") == question.title and key.get("keywords"):
                    keywords_temp = key.get("keywords").replace(" ", "").split(",")
                    keywords = Keyword.objects.filter(name__in=keywords_temp)
                    question.keywords.add(*keywords)
                    question.save()

    def add_experts_to_questions(self, data):
        questions = Question.objects.all()
        for question in questions:
            for key in data:
                if key.get("question") == question.title and key.get("expert"):
                    experts = Expert.objects.filter(name=key.get("expert"))
                    question.experts.add(*experts)
                    question.save()

    def save_to_database(self, obj: object, data: list) -> None:
        obj.objects.bulk_create(data)

    def save_expert_to_database(self, data: list) -> None:
        for expert in data:
            if _file := EXPERTS_FILES.get(expert.name):
                with open(f"backend/management/commands/{_file}", "rb") as f:
                    _actual_file = File(f, name=_file)
                    expert.file = _actual_file
                    expert.save()
                    continue
            expert.save()

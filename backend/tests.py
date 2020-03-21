import json
from django.db.utils import IntegrityError
from django.db import transaction

from django.test import TestCase
from django.core.files import File
from rest_framework.test import APIClient, APITestCase

import mock

from backend.models import Keyword, Question, Answer, Vote, Attachment, Expert


class ModelTests(TestCase):
    """Test database models"""

    def setUp(self):
        self.keyword = Keyword.objects.create(name="coronavirus")
        self.expert = Expert.objects.create(name="dr Coronavirus")
        self.question = Question.objects.create(
            title="Does Corona beer cause COVID-19 desease?",
            real_answer="Coronavirus, a recent flu-like disease spreading worldwide, "
            "has absolutely nothing to do with Corona beer.",
            is_true=False,
        )

    def test_create_keyword(self):
        """Test if keyword can be successfully created"""
        new_keyword = Keyword.objects.create(name="COVID-19")
        self.assertTrue(isinstance(new_keyword, Keyword))
        self.assertEqual(new_keyword.name, "COVID-19")
        self.assertNotEqual(self.keyword, new_keyword)
        self.assertEqual(self.keyword.id, 1)
        self.assertEqual(new_keyword.id, 2)

    def test_create_question(self):
        """Test if question can be successfully created with default values"""
        self.assertTrue(isinstance(self.question, Question))
        question_object = Question.objects.get(id=self.question.id)
        self.assertEqual(
            question_object.title, "Does Corona beer cause COVID-19 desease?"
        )
        self.assertEqual(question_object.down_votes, 0)
        self.assertEqual(question_object.up_votes, 0)
        self.assertEqual(question_object.yes_answers, 0)
        self.assertEqual(question_object.no_answers, 0)
        self.assertEqual(question_object.id, 1)

    def test_assign_keywords_to_question(self):
        """Test if multiple keywords can be assigned to a question ignoring duplicates"""
        new_keyword = Keyword.objects.create(name="COVID-19")
        self.question.keywords.add(self.keyword)
        self.question.keywords.add(new_keyword)
        self.question.keywords.add(new_keyword)
        self.assertEqual(len(self.question.keywords.all()), 2)

    def test_assign_questions_to_keyword(self):
        """Test if multiple questions can be assigned to a keyword ignoring duplicates"""
        new_question = Question.objects.create(
            title="Will garlic prevent the infection?",
            real_answer="The WHO (World Health Organization) says that while it is "
            '"a healthy food that may have some antimicrobial properties", ',
            is_true=False,
        )
        self.keyword.questions.add(self.question)
        self.keyword.questions.add(new_question)
        self.keyword.questions.add(new_question)
        self.assertEqual(len(self.keyword.questions.all()), 2)

    def test_create_answer(self):
        """Test if an answer object can be successfully created"""
        answer = Answer.objects.create(
            question=self.question, sessionID="test123", users_answer=True
        )
        answer_object = Answer.objects.get(id=answer.id)
        self.assertTrue(isinstance(answer, Answer))
        self.assertEqual(answer_object.question, self.question)
        self.assertEqual(answer_object.sessionID, "test123")
        self.assertEqual(answer_object.question.yes_answers, 1)

    def test_create_vote(self):
        """Test if a vote object can be successfully created"""
        vote = Vote.objects.create(
            question=self.question, sessionID="test123", updown=True
        )
        vote_object = Vote.objects.get(id=vote.id)
        self.assertTrue(isinstance(vote, Vote))
        self.assertEqual(vote_object.question, self.question)
        self.assertEqual(vote_object.sessionID, "test123")
        self.assertEqual(vote_object.question.up_votes, 1)

    def test_increment_votes(self):
        """Test if attaching multiple votes will increment counter in question model"""
        Vote.objects.create(question=self.question, sessionID="test123", updown=True)
        Vote.objects.create(
            question=self.question, sessionID="somethingelse", updown=True
        )
        Vote.objects.create(
            question=self.question, sessionID="anothercookie", updown=False
        )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.up_votes, 2)
        self.assertEqual(question_object.down_votes, 1)

    def test_increment_answers(self):
        """Test if attaching multiple answers will increment counter in question model"""
        Answer.objects.create(
            question=self.question, sessionID="test123", users_answer=True
        )
        Answer.objects.create(
            question=self.question, sessionID="somethingelse", users_answer=True
        )
        Answer.objects.create(
            question=self.question, sessionID="anothercookie", users_answer=False
        )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.yes_answers, 2)
        self.assertEqual(question_object.no_answers, 1)

    def test_prevent_duplicate_answers(self):
        """Test if model prevents sending two answers in one session"""
        Answer.objects.create(
            question=self.question, sessionID="test123", users_answer=True
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Answer.objects.create(
                    question=self.question, sessionID="test123", users_answer=True
                )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.yes_answers, 1)

    def test_prevent_duplicate_votes(self):
        """Test if model prevents sending two votes in one session"""
        Vote.objects.create(question=self.question, sessionID="test123", updown=True)
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Vote.objects.create(
                    question=self.question, sessionID="test123", updown=True
                )
                Vote.objects.create(
                    question=self.question, sessionID="test123", updown=False
                )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.up_votes, 1)
        self.assertEqual(question_object.down_votes, 0)

    def test_file_upload(self):
        """Test if a file can be succesfully uploaded"""
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = "test.jpg"
        file_model = Attachment(
            question=self.question, file=file_mock, name=file_mock.name
        )
        self.assertTrue(isinstance(file_model, Attachment))
        self.assertEqual(file_model.name, file_mock.name)

    def test_create_expert(self):
        """Test if expert can be created"""
        new_expert = Expert.objects.create(name="dr Test", website="https://test.pl/")
        self.assertTrue(isinstance(new_expert, Expert))
        self.assertEqual(new_expert.name, "dr Test")
        self.assertNotEqual(self.expert, new_expert)
        self.assertEqual(self.expert.id, 1)
        self.assertEqual(new_expert.id, 2)

    def test_assign_experts_to_question(self):
        """Test if multiple keywords can be assigned to a question ignoring duplicates"""
        new_expert = Expert.objects.create(name="dr Test", website="https://test.pl/")
        self.question.experts.add(self.expert)
        self.question.experts.add(new_expert)
        self.question.experts.add(new_expert)
        self.assertEqual(len(self.question.experts.all()), 2)


class ApiTests(APITestCase):
    def setUp(self):
        Question.objects.create(
            title="Test title",
            real_answer="Real answer",
            is_true=False,
            yes_answers=0,
            no_answers=0,
            up_votes=0,
            down_votes=0,
        )
        Question.objects.create(
            title="Test title2",
            real_answer="Real answer2",
            is_true=True,
            yes_answers=0,
            no_answers=0,
            up_votes=0,
            down_votes=0,
        )
        Keyword.objects.create(name="test keyword")

    def test_can_get_all_questions(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        factory = APIClient()
        response = factory.get("/questions/?format=json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_answer_is_set_when_using_session_id(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 1,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": True,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        Answer.objects.create(
            question=Question.objects.get(pk=1), sessionID="session", users_answer=True
        )
        factory = APIClient()
        response = factory.get("/questions/?format=json&sessionID=session")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_vote_is_set_when_using_session_id(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 1,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": True,
                    "attachments": [],
                    "experts": [],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        Vote.objects.create(
            question=Question.objects.get(pk=1), sessionID="session", updown=True
        )
        factory = APIClient()
        response = factory.get("/questions/?format=json&sessionID=session")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_search_works_by_title(self):
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        factory = APIClient()
        response = factory.get("/questions/?format=json&search=title2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_search_works_by_keyword(self):
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": ["testkeyword"],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        keyword = Keyword.objects.create(name="testkeyword")
        q = Question.objects.get(pk=2)
        q.keywords.add(keyword)
        factory = APIClient()
        response = factory.get("/questions/?format=json&search=testkeyword")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_search_works_by_keyword_and_title(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": ["answer2"],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        keyword = Keyword.objects.create(name="answer2")
        q = Question.objects.get(pk=2)
        q.keywords.add(keyword)
        factory = APIClient()
        response = factory.get("/questions/?format=json&search=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_question_list_contains_attachments(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [{"pk": 1, "name": "testfile", "file": ""}],
                    "experts": [],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = "test.jpg"
        q = Question.objects.get(pk=1)
        att = Attachment.objects.create(question=q, name="testfile", file=file_mock)
        factory = APIClient()
        expected["results"][0]["attachments"][0]["file"] = f"/media/{att.file.name}"
        response = factory.get("/questions/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_question_list_contains_experts(self):
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "pk": 1,
                    "title": "Test title",
                    "is_true": False,
                    "real_answer": "Real answer",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [
                        {
                            "name": "dr Tomasz Rożek",
                            "website": "https://naukatolubie.pl/",
                            "file": None,
                        }
                    ],
                },
                {
                    "pk": 2,
                    "title": "Test title2",
                    "is_true": True,
                    "real_answer": "Real answer2",
                    "yes_answers": 0,
                    "no_answers": 0,
                    "up_votes": 0,
                    "down_votes": 0,
                    "keywords": [],
                    "answers": None,
                    "votes": None,
                    "attachments": [],
                    "experts": [],
                },
            ],
        }
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = "test.jpg"
        q = Question.objects.get(pk=1)
        exp = Expert.objects.create(
            name="dr Tomasz Rożek", website="https://naukatolubie.pl/", file=file_mock
        )
        q.experts.add(exp)
        factory = APIClient()
        expected["results"][0]["experts"][0]["file"] = f"/media/{exp.file.name}"
        response = factory.get("/questions/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_retrieve_object(self):
        """Test if can successfully retrieve a single object"""
        expected = {
            "pk": 1,
            "title": "Test title",
            "is_true": False,
            "real_answer": "Real answer",
            "yes_answers": 0,
            "no_answers": 0,
            "up_votes": 0,
            "down_votes": 0,
            "keywords": [],
            "answers": None,
            "votes": None,
            "attachments": [],
            "experts": [],
        }
        factory = APIClient()
        response = factory.get("/questions/1/?format=json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_object_out_of_range(self):
        """Test if gets an error when attempt to retrieve an object out of range"""
        factory = APIClient()
        response = factory.get("/questions/100/?format=json")
        self.assertEqual(response.status_code, 404)

    def test_if_answer_is_set_when_using_session_id(self):
        """Test if answer is set when user_id is provided"""
        expected = {
            "pk": 1,
            "title": "Test title",
            "is_true": False,
            "real_answer": "Real answer",
            "yes_answers": 1,
            "no_answers": 0,
            "up_votes": 0,
            "down_votes": 0,
            "keywords": [],
            "answers": True,
            "votes": None,
            "attachments": [],
            "experts": [],
        }
        Answer.objects.create(
            question=Question.objects.get(pk=1), sessionID="session", users_answer=True
        )
        factory = APIClient()
        response = factory.get("/questions/1/?format=json&sessionID=session")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(expected)))

    def test_can_add_new_answer(self):
        payload = {"question": 1, "sessionID": "session", "users_answer": True}
        answers = Answer.objects.filter(question__pk=1).count()
        factory = APIClient()
        response = factory.post("/answer/add/", data=payload)
        self.assertEqual(answers + 1, Answer.objects.filter(question__pk=1).count())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(payload)))

    def test_can_add_new_vote(self):
        payload = {"question": 1, "sessionID": "session", "updown": True}
        votes = Vote.objects.filter(question__pk=1).count()
        factory = APIClient()
        response = factory.post("/vote/add/", data=payload)
        self.assertEqual(votes + 1, Vote.objects.filter(question__pk=1).count())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content), json.loads(json.dumps(payload)))

    def test_cannot_add_duplacate_answer(self):
        payload = {"question": 1, "sessionID": "session", "users_answer": True}
        answers = Answer.objects.filter(question__pk=1).count()
        factory = APIClient()
        response = factory.post("/answer/add/", data=payload)
        response = factory.post("/answer/add/", data=payload)
        self.assertEqual(answers + 1, Answer.objects.filter(question__pk=1).count())

    def test_cannot_add_duplicate_vote(self):
        payload = {"question": 1, "sessionID": "session", "updown": True}
        votes = Vote.objects.filter(question__pk=1).count()
        factory = APIClient()
        response = factory.post("/vote/add/", data=payload)
        response = factory.post("/vote/add/", data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(votes + 1, Vote.objects.filter(question__pk=1).count())

import json
from django.db.utils import IntegrityError

from django.test import TestCase, Client
from django.core.files import File
from django.shortcuts import reverse

import mock

from backend.models import (
    Keyword,
    Question,
    Answer,
    Vote,
    Attachment
)


class BackendTests(TestCase):
    def test_can_get_cookie(self):
        c = Client()
        response = c.post(reverse("backend:get_cookie"))
        self.assertIsNotNone(response.client.cookies.items())
        session_id_from_cookie = response.client.cookies["sessionID"].value
        data = json.loads(response.content)
        self.assertEqual(session_id_from_cookie, data.get("sessionID"))

    def test_cookie_dont_change_if_already_set(self):
        c = Client()
        response_first = c.post(reverse("backend:get_cookie"))
        session_id_from_first_cookie = response_first.client.cookies["sessionID"].value
        response_second = c.post(reverse("backend:get_cookie"))
        session_id_from_second_cookie = response_second.client.cookies[
            "sessionID"
        ].value
        data_first = json.loads(response_first.content)
        data_second = json.loads(response_second.content)
        cookie_from_first_data = data_first.get("sessionID")
        cookie_from_second_data = data_second.get("sessionID")
        self.assertEqual(session_id_from_first_cookie, session_id_from_second_cookie)
        self.assertEqual(cookie_from_first_data, cookie_from_second_data)
        self.assertEqual(session_id_from_first_cookie, cookie_from_first_data)
        self.assertEqual(session_id_from_first_cookie, cookie_from_second_data)
        self.assertEqual(session_id_from_second_cookie, cookie_from_first_data)
        self.assertEqual(session_id_from_second_cookie, cookie_from_second_data)


class ModelTests(TestCase):
    """Test database models"""

    def setUp(self):
        self.keyword = Keyword.objects.create(name='coronavirus')
        self.question = Question.objects.create(
            title='Does Corona beer cause COVID-19 desease?',
            real_answer='Coronavirus, a recent flu-like disease spreading worldwide, '
                        'has absolutely nothing to do with Corona beer.',
            is_true=False
        )

    def test_create_keyword(self):
        """Test if keyword can be successfully created"""
        new_keyword = Keyword.objects.create(name='COVID-19')
        self.assertTrue(isinstance(new_keyword, Keyword))
        self.assertEqual(new_keyword.name, 'COVID-19')
        self.assertNotEqual(self.keyword, new_keyword)
        self.assertEqual(self.keyword.id, 1)
        self.assertEqual(new_keyword.id, 2)

    def test_create_question(self):
        """Test if question can be successfully created with default values"""
        self.assertTrue(isinstance(self.question, Question))
        question_object = Question.objects.get(id=self.question.id)
        self.assertEqual(question_object.title, 'Does Corona beer cause COVID-19 desease?')
        self.assertEqual(question_object.down_votes, 0)
        self.assertEqual(question_object.up_votes, 0)
        self.assertEqual(question_object.yes_answers, 0)
        self.assertEqual(question_object.no_answers, 0)
        self.assertEqual(question_object.id, 1)

    def test_assign_keywords_to_question(self):
        """Test if multiple keywords can be assigned to a question ignoring duplicates"""
        new_keyword = Keyword.objects.create(name='COVID-19')
        self.question.keywords.add(self.keyword)
        self.question.keywords.add(new_keyword)
        self.question.keywords.add(new_keyword)
        self.assertEqual(len(self.question.keywords.all()), 2)

    def test_assign_questions_to_keyword(self):
        """Test if multiple questions can be assigned to a keyword ignoring duplicates"""
        new_question = Question.objects.create(
            title='Will garlic prevent the infection?',
            real_answer='The WHO (World Health Organization) says that while it is '
                        '"a healthy food that may have some antimicrobial properties", ',
            is_true=False
        )
        self.keyword.questions.add(self.question)
        self.keyword.questions.add(new_question)
        self.keyword.questions.add(new_question)
        self.assertEqual(len(self.keyword.questions.all()), 2)

    def test_create_answer(self):
        """Test if an answer object can be successfully created"""
        answer = Answer.objects.create(
            question=self.question,
            sessionID='test123',
            users_answer=True
        )
        answer_object = Answer.objects.get(id=answer.id)
        self.assertTrue(isinstance(answer, Answer))
        self.assertEqual(answer_object.question, self.question)
        self.assertEqual(answer_object.sessionID, 'test123')
        self.assertEqual(answer_object.question.yes_answers, 1)

    def test_create_vote(self):
        """Test if a vote object can be successfully created"""
        vote = Vote.objects.create(
            question=self.question,
            sessionID='test123',
            updown=True
        )
        vote_object = Vote.objects.get(id=vote.id)
        self.assertTrue(isinstance(vote, Vote))
        self.assertEqual(vote_object.question, self.question)
        self.assertEqual(vote_object.sessionID, 'test123')
        self.assertEqual(vote_object.question.up_votes, 1)

    def test_increment_votes(self):
        """Test if attaching multiple votes will increment counter in question model"""
        Vote.objects.create(
            question=self.question,
            sessionID='test123',
            updown=True
        )
        Vote.objects.create(
            question=self.question,
            sessionID='somethingelse',
            updown=True
        )
        Vote.objects.create(
            question=self.question,
            sessionID='anothercookie',
            updown=False
        )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.up_votes, 2)
        self.assertEqual(question_object.down_votes, 1)

    def test_increment_answers(self):
        """Test if attaching multiple answers will increment counter in question model"""
        Answer.objects.create(
            question=self.question,
            sessionID='test123',
            users_answer=True
        )
        Answer.objects.create(
            question=self.question,
            sessionID='somethingelse',
            users_answer=True
        )
        Answer.objects.create(
            question=self.question,
            sessionID='anothercookie',
            users_answer=False
        )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.yes_answers, 2)
        self.assertEqual(question_object.no_answers, 1)

    def test_prevent_duplicate_answers(self):
        """Test if model prevents sending two answers in one session"""
        Answer.objects.create(
            question=self.question,
            sessionID='test123',
            users_answer=True
        )
        with self.assertRaises(IntegrityError):
            Answer.objects.create(
                question=self.question,
                sessionID='test123',
                users_answer=True
            )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object, 1)

    def test_prevent_duplicate_votes(self):
        """Test if model prevents sending two votes in one session"""
        Vote.objects.create(
            question=self.question,
            sessionID='test123',
            updown=True
        )
        with self.assertRaises(IntegrityError):
            Vote.objects.create(
                question=self.question,
                sessionID='test123',
                updown=True
            )
            Vote.objects.create(
                question=self.question,
                sessionID='test123',
                updown=False
            )
        question_object = Question.objects.get(title=self.question.title)
        self.assertEqual(question_object.up_votes, 1)
        self.assertEqual(question_object.down_votes, 0)

    def test_file_upload(self):
        """Test if a file can be succesfully uploaded"""
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.jpg'
        file_model = Attachment(
            question=self.question,
            file=file_mock,
            name=file_mock.name
        )
        self.assertTrue(isinstance(file_model, Attachment))
        self.assertEqual(file_model.name, file_mock.name)

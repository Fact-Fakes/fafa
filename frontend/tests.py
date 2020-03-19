import json
from django.test import TestCase, Client
from django.shortcuts import reverse


class FrontendTests(TestCase):
    def test_cookie_is_set_on_index_page(self):
        c = Client()
        response = c.get(reverse("frontend:index"))
        self.assertIsNotNone(response.client.cookies.items())
        session_id_from_cookie = response.client.cookies["sessionID"].value
        self.assertIsNotNone(session_id_from_cookie)

    def test_cookie_dont_change_when_opening_page_again(self):
        c = Client()
        response_first = c.get(reverse("frontend:index"))
        session_id_from_first_cookie = response_first.client.cookies["sessionID"].value
        response_second = c.get(reverse("frontend:index"))
        session_id_from_second_cookie = response_second.client.cookies[
            "sessionID"
        ].value
        self.assertEqual(session_id_from_first_cookie, session_id_from_second_cookie)

    def test_cookie_is_the_same_in_backend(self):
        c = Client()
        response_first = c.get(reverse("frontend:index"))
        session_id_from_first_frontend = response_first.client.cookies[
            "sessionID"
        ].value
        response = c.post(reverse("backend:get_cookie"))
        data = json.loads(response.content)
        cookie_from_backend = response.client.cookies["sessionID"].value
        cookie_from_data_backend = data.get("sessionID")
        self.assertEqual(cookie_from_backend, cookie_from_data_backend)
        response = c.get(reverse("frontend:index"))
        self.assertIsNotNone(response.client.cookies.items())
        cookie_from_frontend = response.client.cookies["sessionID"].value
        self.assertIsNotNone(cookie_from_frontend)
        self.assertEqual(cookie_from_backend, cookie_from_frontend)
        self.assertEqual(cookie_from_data_backend, cookie_from_frontend)

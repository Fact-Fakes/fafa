import json
from django.test import TestCase, Client
from django.shortcuts import reverse


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

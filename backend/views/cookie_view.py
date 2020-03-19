from django.views import View
from django.http import JsonResponse


class CookieView(View):
    def post(self, request):
        if session_from_cookie := request.COOKIES.get("sessionID"):
            return JsonResponse({"sessionID": session_from_cookie})
        session_id = request.session._get_or_create_session_key()
        response = JsonResponse({"sessionID": session_id})
        response.set_cookie("sessionID", session_id)
        return response


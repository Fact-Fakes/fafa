from django.views import View
from django.http import HttpResponse

# * This View is just placeholder for main View
# * Just adding cookie setter
class IndexView(View):
    def get(self, request):
        response = HttpResponse("OK")
        if session_from_cookie := request.COOKIES.get("sessionID"):
            return response
        session_id = request.session._get_or_create_session_key()
        response.set_cookie("sessionID", session_id)
        return response

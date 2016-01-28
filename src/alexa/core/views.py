from django.http import HttpResponse
from django.views.generic import View


class DispatcherView(View):
    def get(self, request):
        return HttpResponse("Welcome to the rockman household alexa integration")

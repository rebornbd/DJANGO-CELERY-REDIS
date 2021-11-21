from django.http import HttpResponse
from .tasks import add, mul


def home(request):
  # celery task assign
  add.delay(10, 10)

  # get user response as possible
  return HttpResponse("done!")

import pathlib

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

from environs import Env


env = Env()
env.read_env()

BASE_DIR = pathlib.Path(__file__).parent

if not settings.configured:
    settings.configure(
        SECRET_KEY=env.str("DJANGO_SECRET_KEY"),
        DEBUG=env.bool("DJANGO_DEBUG"),
        ROOT_URLCONF="static-tex",
    )


def index(request):
    return HttpResponse("Installation successful.")


urlpatterns = [
    path("", index, name="index"),
]

if __name__ == "__main__":
    import sys
    execute_from_command_line(sys.argv)

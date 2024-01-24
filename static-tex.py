import os
import pathlib
import subprocess
import argparse

from django.conf import settings
from django.core.management import execute_from_command_line, call_command
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import path
from django.shortcuts import render

from environs import Env


env = Env()
env.read_env()

BASE_DIR = pathlib.Path(__file__).parent

if not settings.configured:
    settings.configure(
        SECRET_KEY=env.str("DJANGO_SECRET_KEY"),
        DEBUG=env.bool("DJANGO_DEBUG"),
        ROOT_URLCONF="static-tex",
        TEX_SOURCE_DIR=BASE_DIR / "tex_src",
        TEX_BUILD_DIR=BASE_DIR / "html_out",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [BASE_DIR],
            }
        ],
        STATIC_ROOT=BASE_DIR / "html_out",
        INSTALLED_APPS=(
            "static_tex",
        )
    )


def page(request, slug):

    # html_dir = BASE_DIR / "html_out" / slug
    html_file = f"html_out/{slug}/index.html"

    return render(request, html_file)


urlpatterns = [
    path("<slug:slug>", page, name="index"),
]

if __name__ == "__main__":
    import sys
    execute_from_command_line(sys.argv)


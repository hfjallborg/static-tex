import os
import pathlib
import shutil
import subprocess
import tempfile

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Builds .tex files into html"

    def handle(self, *args, **options):

        if pathlib.Path(settings.TEX_BUILD_DIR).exists():
            shutil.rmtree(settings.TEX_BUILD_DIR)

        for src_file in pathlib.Path(settings.TEX_SOURCE_DIR).glob("*.tex"):
            wd = os.getcwd()
            os.chdir(settings.TEX_SOURCE_DIR)
            output_dir = settings.TEX_BUILD_DIR / src_file.stem
            p = subprocess.Popen(["plastex", "-d", output_dir, "--split-level", "-2", src_file.name])
            p.wait()
            os.chdir(wd)

from django.core.management.base import BaseCommand
import sys
import optparse
from tunes.models import *

class Command(BaseCommand):
    help = 'Imports tsv copied and pasted from *my* iTunes'
    args = 'import_file'

    def handle(self, import_file, **options):
        with open(import_file) as f:
            lines = [line for line in f.readlines() if len(line.strip()) > 0]
        for line in lines:
            song = Song()
            song.deserialize_itunes_tsv(line)
            song.save()


from . import *
from io import StringIO
from django.core.management import call_command


class Commands(TestCase):

    def test_populate(self):
        out = StringIO()
        call_command('populate', stdout=out)
        self.assertNotEqual("Error populating database.", out.getvalue())

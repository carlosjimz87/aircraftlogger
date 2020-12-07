from . import *
from io import StringIO
from django.core.management import call_command


class Commands(TestCase):

    def test_populate_airports(self):
        out = StringIO()
        call_command('populate_airports', stdout=out)
        print(out.getvalue())
        self.assertIn("Successfully created ", out.getvalue())

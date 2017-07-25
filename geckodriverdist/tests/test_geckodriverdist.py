from subprocess import check_call
from unittest import TestCase


class TestGeckoDriverDist(TestCase):

    def test_geckodriver_in_path(self):
        check_call(['geckodriver', '--version'])

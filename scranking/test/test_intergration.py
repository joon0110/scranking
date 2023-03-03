import unittest
from scranking.Swimmer import Swimmer
from bs4 import BeautifulSoup

class TestIntergration(unittest.TestCase):
    def test_swimmer(self):
        url = 'https://www.swimcloud.com/swimmer/549377/'
        swimmer = Swimmer(url)
        infohtml = '<ul class="o-list-inline o-list-inline--dotted"><li>Katy, TX</li><li><a href="/team/283">Columbia University</a></li><li><ul class="o-list-inline"><li class="u-mr-"><a class="btn-icon-plain" href="https://twitter.com/SeungjoonA" target="_blank" title="Twitter"><i class="fab fa-twitter"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Twitter</span></a></li><li><a class="btn-icon-plain" href="https://instagram.com/seun_g01" target="_blank" title="Instagram"><i class="fab fa-instagram"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Instagram</span></a></li></ul></li></ul>'

        # Check HTTP status
        self.assertEqual(swimmer.get_http_status(), 200)

        # Check that soup was successfully parsed
        soup = swimmer.get_soup()
        self.assertIsInstance(soup, BeautifulSoup)

        # Check name extraction
        self.assertEqual(swimmer.get_name(soup), "Seungjoon Ahn")
        extractinfo = swimmer.get_info(infohtml)
        self.assertEqual(extractinfo, ("Katy, TX", "Columbia University", "https://twitter.com/SeungjoonA", "https://instagram.com/seun_g01"))
        
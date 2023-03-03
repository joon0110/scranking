from scranking.Swimmer import Swimmer
from bs4 import BeautifulSoup


def test_swimmer(self):
    url = 'https://www.swimcloud.com/swimmer/549377/'
    swimmer = Swimmer(url)
    infohtml = '<ul class="o-list-inline o-list-inline--dotted"><li>Katy, TX</li><li><a href="/team/283">Columbia University</a></li><li><ul class="o-list-inline"><li class="u-mr-"><a class="btn-icon-plain" href="https://twitter.com/SeungjoonA" target="_blank" title="Twitter"><i class="fab fa-twitter"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Twitter</span></a></li><li><a class="btn-icon-plain" href="https://instagram.com/seun_g01" target="_blank" title="Instagram"><i class="fab fa-instagram"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Instagram</span></a></li></ul></li></ul>'

    soup = swimmer.get_soup()
    swimmer.get_info(infohtml)
    assert swimmer.get_http_status() == 200
    assert swimmer.get_name(soup) == "Seungjoon Ahn"

    assert swimmer.get_info(infohtml) == "Katy, TX\nColumbia University\nhttps://twitter.com/SeungjoonA\nhttps://instagram.com/seun_g01\n"
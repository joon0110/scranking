from scranking.Swimmer import Swimmer


def test_swimmer():
    url = 'https://www.swimcloud.com/swimmer/549377/'
    swimmer = Swimmer(url)

    soup = swimmer.get_soup()
    assert swimmer.get_http_status() == 200
    assert swimmer.get_name(soup) == "Seungjoon Ahn"

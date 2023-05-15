from scranking.Swimmer import Swimmer


def test_swimmer():
    url = 'https://www.swimcloud.com/swimmer/549377/'
    swimmer = Swimmer(url)

    soup = swimmer.get_soup()
    assert swimmer.get_http_status() == 200
    assert swimmer.get_name(soup) == "Seungjoon Ahn"


def test_get_info():
    url = 'https://www.swimcloud.com/swimmer/549377/'
    expected_info = (
        "Hometown: Katy, TX, "
        "University: Columbia University, "
        "Twitter: https://twitter.com/SeungjoonA, "
        "Instagram: https://instagram.com/seun_g01"
    )
    swimmer = Swimmer(url)
    soup = swimmer.get_soup()
    info = swimmer.get_info(soup)
    assert info == expected_info

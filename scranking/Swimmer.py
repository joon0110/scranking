import requests
from bs4 import BeautifulSoup


class Swimmer:
    def __init__(self, url):
        self.url = url

    def get_http_status(self):
        response = requests.get(self.url)
        if not response:
            return "Connection fail"
        else:
            return response.status_code

    def get_soup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if not soup:
            return "Not possible to parse"
        else:
            return soup

    def save_soup_to_file(self, soup, filename):
        with open(filename, "w") as f:
            f.write(str(soup))

    def get_name(self, soup):
        name = soup.find('title')
        titleString = name.string
        s1 = titleString.replace("| Swimcloud", "", 1).replace('\n', '').strip()  # noqa

        if not s1:
            return None
        else:
            return s1

    def get_info(self, html):
        newsoup = BeautifulSoup(html, 'html.parser')
        hometown = newsoup.find('li').get_text()
        print(hometown)
        university = newsoup.find('a').get_text()
        print(university)

        social_links = newsoup.find_all('a', class_='btn-icon-plain')
        for link in social_links:
            title = link.get('title')
            if 'Twitter' in title:
                twitter = link['href']
                print(twitter)
            elif 'Instagram' in title:
                instagram = link['href']
                print(instagram)


url = 'https://www.swimcloud.com/swimmer/549377/'
swimmer = Swimmer(url)
http_status = swimmer.get_http_status()
soup = swimmer.get_soup()
swimmer.save_soup_to_file(soup, "schml.txt")
infohtml = '<ul class="o-list-inline o-list-inline--dotted"><li>Katy, TX</li><li><a href="/team/283">Columbia University</a></li><li><ul class="o-list-inline"><li class="u-mr-"><a class="btn-icon-plain" href="https://twitter.com/SeungjoonA" target="_blank" title="Twitter"><i class="fab fa-twitter"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Twitter</span></a></li><li><a class="btn-icon-plain" href="https://instagram.com/seun_g01" target="_blank" title="Instagram"><i class="fab fa-instagram"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Instagram</span></a></li></ul></li></ul>'  # noqa

name = swimmer.get_name(soup)
print(url)
print("HTTP status:", http_status)
print(name)
swimmer.get_info(infohtml)

import requests
from bs4 import BeautifulSoup


class Swimmer:
    """
    A class representing a swimmer for Swimcloud website
    """

    def __init__(self, url):
        """
        Initialize the Swimmer object.
        """
        self.url = url
        self.event_list = []

    def get_http_status(self):
        """
        Check if the Swimcloud website is working.

        :return: The status code of the website.
        """
        response = requests.get(self.url)
        if not response:
            return "Connection fail"
        else:
            return response.status_code

    def get_soup(self):
        """
        Create a bf4 for the input url.

        :return: BeautifulSoup of the input url.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if not soup:
            return "Not possible to parse"
        else:
            return soup

    def save_soup_to_file(self, soup, filename):
        """
        Create a txt file that contains the html of the input website to see with eyes.

        """
        with open(filename, "w") as f:
            f.write(str(soup))

    def get_name(self, soup):
        """
        Gets the name of the swimmer.

        :param soup: The BeautifulSoup you created from get_soup() method.
        :return: A full name of the swimmer.
        """
        name = soup.find('title')
        titleString = name.string
        s1 = titleString.replace("| Swimcloud", "", 1).replace('\n', '').strip()  # noqa

        if not s1:
            return None
        else:
            return s1

    def get_info(self, html):
        """
        Get the social network informnations of the swimmer
        """
        newsoup = BeautifulSoup(html, 'html.parser')
        hometown = newsoup.find('li').get_text()
        university = newsoup.find('a').get_text()

        social_links = newsoup.find_all('a', class_='btn-icon-plain')
        for link in social_links:
            title = link.get('title')
            if 'Twitter' in title:
                twitter = link['href']
            elif 'Instagram' in title:
                instagram = link['href']

        return f"Hometown: {hometown}, University: {university}, Twitter: {twitter}, Instagram: {instagram}"  # noqa

    def get_event(self, html):
        newsoup = BeautifulSoup(html, 'html.parser')
        rows = newsoup.select('#js-swimmer-profile-times-container tbody tr')

        results = []
        for row in rows:
            event_name = row.select_one('td:nth-of-type(1)').text.strip()
            time = row.select_one('td:nth-of-type(2) a').text.strip()
            results.append(f'{event_name}: {time}')
        self.event_list = results

        return results

    def lookup_event(self, event_name):
        for event in self.event_list:
            if event_name in event:
                return event
        return f'{event_name} not found'


# still working lines below.
url = 'https://www.swimcloud.com/swimmer/549377/'
swimmer = Swimmer(url)
http_status = swimmer.get_http_status()
soup = swimmer.get_soup()
# swimmer.save_soup_to_file(soup, "schml.txt")
infohtml = '<ul class="o-list-inline o-list-inline--dotted"><li>Katy, TX</li><li><a href="/team/283">Columbia University</a></li><li><ul class="o-list-inline"><li class="u-mr-"><a class="btn-icon-plain" href="https://twitter.com/SeungjoonA" target="_blank" title="Twitter"><i class="fab fa-twitter"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Twitter</span></a></li><li><a class="btn-icon-plain" href="https://instagram.com/seun_g01" target="_blank" title="Instagram"><i class="fab fa-instagram"></i><span class="u-is-hidden-visually">Seungjoon Ahn on Instagram</span></a></li></ul></li></ul>'  # noqa
eventhtml = '</div> </div> <div class="col-sm-12"> <div class="c-card c-card--large o-grid__col-span-2" id="js-swimmer-profile-times"> <div class="c-card__item"> <ul class="c-tabs u-mb js-swimmer-profile-times-options"> <li class="c-tabs__item active"> <a class="c-tabs__link u-text-truncate" href="/swimmer/549377/times/fastest/"> PERSONAL BESTS </a> </li> <li class="c-tabs__item"> <a class="c-tabs__link u-text-truncate" href="/swimmer/549377/times/byevent/"> EVENT PROGRESSION </a> </li> </ul> <div id="js-swimmer-profile-times-container"> <div class="c-table-clean--responsive"> <table class="c-table-clean c-table-clean--middle table table-hover"> <thead> <tr> <th>Event</th> <th class="c-table-clean__col-fit u-text-end">Time</th> <th class="c-table-clean__col-fit hidden-xs"></th> <th class="hidden-xs">Meet</th> <th class="c-table-clean__col-fit">Date</th> </tr> </thead> <tbody> <tr> <td class="u-text-truncate">50 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/241307/event/8/?id=90394357#time90394357">21.02</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/241307">Princeton Big Al Invitational</a> </td> <td class="u-text-truncate">Dec 02, 2022</td> </tr> <tr> <td class="u-text-truncate">50 L Free</td> <td class="u-text-end u-text-semi"> <a href="/results/96679/event/6/?id=12249757#time12249757">25.98</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <span class="c-label c-label--neutral u-is-helpable" title="Relay Leadoff"> R </span> </td> <td class="hidden-xs"> <a href="/results/96679">Southern Zone Senior Championships</a> </td> <td class="u-text-truncate">Aug 01, 2017</td> </tr> <tr> <td class="u-text-truncate">100 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/241307/event/34/?id=90394542#time90394542">45.70</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/241307">Princeton Big Al Invitational</a> </td> <td class="u-text-truncate">Dec 04, 2022</td> </tr> <tr> <td class="u-text-truncate">100 L Free</td> <td class="u-text-end u-text-semi"> <a href="/results/148868/event/36/?id=27527423#time27527423">54.74</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <span class="c-label c-label--neutral u-is-helpable" title="Relay Leadoff"> R </span> </td> <td class="hidden-xs"> <a href="/results/148868">GU TWST Senior LC Invite</a> </td> <td class="u-text-truncate">Jun 30, 2019</td> </tr> <tr> <td class="u-text-truncate">200 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/165768/event/4/?id=34535870#time34535870">1:37.85</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/165768">UIL 6A State Championship</a> </td> <td class="u-text-truncate">Feb 14, 2020</td> </tr> <tr> <td class="u-text-truncate">200 L Free</td> <td class="u-text-end u-text-semi"> <a href="/results/130301/event/19/?id=28638000#time28638000">1:53.71</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <span class="c-label c-label--neutral u-is-helpable" title="Relay Leadoff"> R </span> </td> <td class="hidden-xs"> <a href="/results/130301">NCSA Summer Championship</a> </td> <td class="u-text-truncate">Aug 07, 2019</td> </tr> <tr> <td class="u-text-truncate">400 L Free</td> <td class="u-text-end u-text-semi"> <a href="/results/173714/event/12/?id=35085701#time35085701">4:03.81</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/173714">Speedo Champions Series - College Station</a> </td> <td class="u-text-truncate">Feb 28, 2020</td> </tr> <tr> <td class="u-text-truncate">500 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/165768/event/16/?id=34535907#time34535907">4:21.68</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/165768">UIL 6A State Championship</a> </td> <td class="u-text-truncate">Feb 14, 2020</td> </tr> <tr> <td class="u-text-truncate">1000 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/127953/event/4/?id=41418568#time41418568">10:01.87</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/127953">GU KATY Quad College Format</a> </td> <td class="u-text-truncate">Dec 28, 2018</td> </tr> <tr> <td class="u-text-truncate">1500 L Free</td> <td class="u-text-end u-text-semi"> <a href="/results/95206/event/40/?id=11920739#time11920739">17:26.37</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/95206">ST AAAA Northside George Block Invitational</a> </td> <td class="u-text-truncate">Jun 25, 2017</td> </tr> <tr> <td class="u-text-truncate">1650 Y Free</td> <td class="u-text-end u-text-semi"> <a href="/results/215290/event/8/?id=51252912#time51252912">16:55.64</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/215290">Third Coast Invitational hoste</a> </td> <td class="u-text-truncate">Jan 13, 2017</td> </tr> <tr> <td class="u-text-truncate">50 Y Back</td> <td class="u-text-end u-text-semi"> <a href="/results/171004/event/22/?id=31269395#time31269395">27.33</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <span class="c-label c-label--neutral u-is-helpable" title="Extracted"> X </span> </td> <td class="hidden-xs"> <a href="/results/171004">GU TWST Southern Senior Championships</a> </td> <td class="u-text-truncate">Dec 07, 2019</td> </tr> <tr> <td class="u-text-truncate">50 L Back</td> <td class="u-text-end u-text-semi"> <a href="/results/96434/event/8/?id=12171551#time12171551">34.73</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/96434">Gulf Swimming Senior Championships</a> </td> <td class="u-text-truncate">Jul 14, 2017</td> </tr> <tr> <td class="u-text-truncate">100 Y Back</td> <td class="u-text-end u-text-semi"> <a href="/results/171004/event/22/?id=31269395#time31269395">56.47</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/171004">GU TWST Southern Senior Championships</a> </td> <td class="u-text-truncate">Dec 07, 2019</td> </tr> <tr> <td class="u-text-truncate">100 L Back</td> <td class="u-text-end u-text-semi"> <a href="/results/95206/event/34/?id=11916822#time11916822">1:11.38</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/95206">ST AAAA Northside George Block Invitational</a> </td> <td class="u-text-truncate">Jun 25, 2017</td> </tr> <tr> <td class="u-text-truncate">200 Y Back</td> <td class="u-text-end u-text-semi"> <a href="/results/197581/event/20/?id=41417809#time41417809">2:06.83</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/197581">GU KATY Katy Quince Meet</a> </td> <td class="u-text-truncate">Oct 21, 2018</td> </tr> <tr> <td class="u-text-truncate">200 L Back</td> <td class="u-text-end u-text-semi"> <a href="/results/117546/event/18/?id=18611924#time18611924">2:31.41</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/117546">GU KATY Senior Invite</a> </td> <td class="u-text-truncate">May 20, 2018</td> </tr> <tr> <td class="u-text-truncate">50 Y Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/197580/event/8/?id=41416126#time41416126">29.69</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/197580">Katy Purple &amp; Black Meet</a> </td> <td class="u-text-truncate">Sep 22, 2018</td> </tr> <tr> <td class="u-text-truncate">50 L Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/96434/event/34/?id=12171758#time12171758">35.65</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/96434">Gulf Swimming Senior Championships</a> </td> <td class="u-text-truncate">Jul 16, 2017</td> </tr> <tr> <td class="u-text-truncate">100 Y Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/162612/event/6/?id=41412895#time41412895">1:02.65</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/162612">GU PACK October Open</a> </td> <td class="u-text-truncate">Oct 12, 2019</td> </tr> <tr> <td class="u-text-truncate">100 L Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/95103/event/12/?id=11877942#time11877942">1:15.69</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/95103">GU TWST Senior Open Meet</a> </td> <td class="u-text-truncate">May 20, 2017</td> </tr> <tr> <td class="u-text-truncate">200 Y Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/197581/event/26/?id=41417580#time41417580">2:16.99</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/197581">GU KATY Katy Quince Meet</a> </td> <td class="u-text-truncate">Oct 21, 2018</td> </tr> <tr> <td class="u-text-truncate">200 L Breast</td> <td class="u-text-end u-text-semi"> <a href="/results/215396/event/6/?id=51464622#time51464622">2:44.88</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/215396">PLAT/KATY IMX Meet</a> </td> <td class="u-text-truncate">Apr 29, 2017</td> </tr> <tr> <td class="u-text-truncate">50 Y Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/263969/event/9/?id=97777537#time97777537">22.18</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <span class="c-label c-label--neutral u-is-helpable" title="Extracted"> X </span> </td> <td class="hidden-xs"> <a href="/results/263969">Ivy League Championships (M)</a> </td> <td class="u-text-truncate">Feb 24, 2023</td> </tr> <tr> <td class="u-text-truncate">50 L Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/130301/event/10/?id=28636063#time28636063">25.37</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/130301">NCSA Summer Championship</a> </td> <td class="u-text-truncate">Aug 06, 2019</td> </tr> <tr> <td class="u-text-truncate">100 Y Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/263969/event/9/?id=97777538#time97777538">47.41</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <a href="/results/236950"> <span class="c-label c-label--outline c-label--warning" title="NCAA Division I Mens Championships"> B </span> </a> </td> <td class="hidden-xs"> <a href="/results/263969">Ivy League Championships (M)</a> </td> <td class="u-text-truncate">Feb 24, 2023</td> </tr> <tr> <td class="u-text-truncate">100 L Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/150274/event/318/?id=28453763#time28453763">55.41</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/150274">Phillips 66 Summer National Time Trials</a> </td> <td class="u-text-truncate">Aug 02, 2019</td> </tr> <tr> <td class="u-text-truncate">200 Y Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/224466/event/19/?id=59693509#time59693509">1:43.75</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <a href="/results/194776"> <span class="c-label c-label--outline c-label--warning" title="NCAA Division I Mens Championship"> B </span> </a> </td> <td class="hidden-xs"> <a href="/results/224466">Ivy League Championships (M)</a> </td> <td class="u-text-truncate">Feb 26, 2022</td> </tr> <tr> <td class="u-text-truncate">200 L Fly</td> <td class="u-text-end u-text-semi"> <a href="/results/114384/event/2/?id=19932245#time19932245">2:01.36</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> <a href="/results/130512"> <span class="c-label c-label--outline c-label--success" title="USA Swimming Winter National Championships"> A </span> </a> </td> <td class="hidden-xs"> <a href="/results/114384">Speedo Junior National Championships</a> </td> <td class="u-text-truncate">Jul 31, 2018</td> </tr> <tr> <td class="u-text-truncate">200 Y IM</td> <td class="u-text-end u-text-semi"> <a href="/results/173714/event/34/?id=35081136#time35081136">1:53.76</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/173714">Speedo Champions Series - College Station</a> </td> <td class="u-text-truncate">Mar 01, 2020</td> </tr> <tr> <td class="u-text-truncate">200 L IM</td> <td class="u-text-end u-text-semi"> <a href="/results/173714/event/34/?id=35081137#time35081137">2:12.30</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/173714">Speedo Champions Series - College Station</a> </td> <td class="u-text-truncate">Mar 01, 2020</td> </tr> <tr> <td class="u-text-truncate">400 Y IM</td> <td class="u-text-end u-text-semi"> <a href="/results/204391/event/16/?id=49075246#time49075246">4:12.33</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/204391">Princeton BIG AL INVITATIONAL</a> </td> <td class="u-text-truncate">Dec 04, 2021</td> </tr> <tr> <td class="u-text-truncate">400 L IM</td> <td class="u-text-end u-text-semi"> <a href="/results/117546/event/16/?id=18611849#time18611849">4:59.49</a> </td> <td class="u-pl0 u-nowrap hidden-xs"> </td> <td class="hidden-xs"> <a href="/results/117546">GU KATY Senior Invite</a> </td> <td class="u-text-truncate">May 19, 2018</td> </tr> </tbody> </table> </div> </div>'  # noqa
name = swimmer.get_name(soup)
print(url)
print("HTTP status:", http_status)
print(name)
info = swimmer.get_info(infohtml)
print(info)
event = swimmer.get_event(eventhtml)
print(event)
lookupcheck = swimmer.lookup_event("40 L Free")
print(lookupcheck)

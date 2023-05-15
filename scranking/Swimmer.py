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
        Create a txt file that contains the html of the input website to
        see with eyes.
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

    def get_info(self, soup: BeautifulSoup) -> str:
        """
        Get the social network informnations of the swimmer.

        :param soup: The BeautifulSoup you created from get_soup() method.
        :return: A string containing the name ofhometown, university,
        Twitter, and Instagram.
        """

        info_element = soup.find('ul', class_='o-list-inline o-list-inline--dotted')
        hometown = info_element.find('li').text
        university = info_element.find('a').text

        social_networks_links = info_element.find_all('a', class_='btn-icon-plain')

        twitter = ''
        instagram = ''

        for link in social_networks_links:
            if 'Twitter' in link.get('title'):
                twitter = link.get('href')
            if 'Instagram' in link.get('title'):
                instagram = link.get('href')

        return f"Hometown: {hometown}, University: {university}," f" Twitter: {twitter}, Instagram: {instagram}"

    def get_event(self, soup):
        """
        Gets all the swimmer's events with best time.

        :param soup: The BeautifulSoup you created from get_soup() method.
        :return: A list containing events and times.
        """
        rows = soup.select('#js-swimmer-profile-times-container tbody tr')

        results = []
        for row in rows:
            event_name = row.select_one('td:nth-of-type(1)').text.strip()
            time = row.select_one('td:nth-of-type(2) a').text.strip()
            results.append(f'{event_name}: {time}')
        self.event_list = results

        return results

    def lookup_event(self, event_name):
        """
        Gets event and a best time.

        :param event_name: An event you want to search for.
        :return: An event with a best time. If there is no such event, returns not found
        """
        for event in self.event_list:
            if event_name in event:
                return event
        return f'{event_name} not found'

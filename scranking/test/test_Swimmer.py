import unittest
from unittest.mock import MagicMock, patch
from scranking.Swimmer import Swimmer
from bs4 import BeautifulSoup


class TestSwimmer(unittest.TestCase):
    @patch('requests.get')
    def test_get_http_status_if_response(self, mock_get):
        swimmer = Swimmer("http://www.example.com")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        self.assertEqual(swimmer.get_http_status(), 200)

    @patch('requests.get')
    def test_get_http_status_if_not_response(self, mock_get):
        swimmer = Swimmer("http://www.example.com")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = None

        self.assertEqual(swimmer.get_http_status(), "Connection fail")

    @patch('requests.get')
    def test_get_soup_if_soup(self, mock_get):
        swimmer = Swimmer("http://www.example.com")
        mock_response = MagicMock()
        mock_response.content = b'<html><body></body></html>'
        mock_get.return_value = mock_response

        soup = swimmer.get_soup()

        self.assertIsInstance(soup, BeautifulSoup)

    def test_save_soup_to_file(self):
        swimmer = Swimmer("http://www.example.com")
        soup = BeautifulSoup('<html><body></body></html>', 'html.parser')

        filename = "test.html"
        swimmer.save_soup_to_file(soup, filename)

        with open(filename, "r") as f:
            file_content = f.read()

        self.assertEqual(file_content, str(soup))

    def test_get_name_with_valid_input(self):
        swimmer = Swimmer("https://example.com")
        html_doc = '<html><head><title>Sample Title ' '| Swimcloud</title></head></html>'  # noqa
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Call the function and check the output
        self.assertEqual(swimmer.get_name(soup), "Sample Title")

    def test_get_name_with_not_valid_input(self):
        swimmer = Swimmer("https://example.com")
        html_doc = '<html><head><title> | Swimcloud</title></head></html>'
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Call the function and check the output
        self.assertEqual(swimmer.get_name(soup), None)

    @patch('requests.get')
    def test_get_info(self, mock_get):
        swimmer = Swimmer("http://www.example.com")
        mock_response = MagicMock()
        mock_response.content = b'<html><body><li>Hometown</li><a>University</a></body></html>'  # noqa
        mock_get.return_value = mock_response

        html_doc = (
            '<html><body><li>Hometown</li><a>University</a>'
            '<a class="btn-icon-plain" title="Twitter" href="twitter.com"></a>'
            '<a class="btn-icon-plain" title="Instagram" href="instagram.com"></a>'
            '</body></html>'
        )
        expected_output = (
            "Hometown: Hometown, University: University, " "Twitter: twitter.com, Instagram: instagram.com"
        )
        soup = BeautifulSoup(html_doc, 'html.parser')

        self.assertEqual(swimmer.get_info(html_doc), expected_output)

    def test_get_event(self):
        swimmer = Swimmer("http://www.example.com")

        html_doc = (
            '<html><body><table id="js-swimmer-profile-times-container"><tbody>'
            '<tr><td>Event 1</td><td><a>Time 1</a></td></tr>'
            '<tr><td>Event 2</td><td><a>Time 2</a></td></tr>'
            '</tbody></table></body></html>'
        )
        expected_output = ['Event 1: Time 1', 'Event 2: Time 2']
        soup = BeautifulSoup(html_doc, 'html.parser')

        self.assertEqual(swimmer.get_event(soup), expected_output)

    def test_lookup_event_found(self):
        swimmer = Swimmer("http://www.example.com")
        swimmer.event_list = ['Event 1: Time 1', 'Event 2: Time 2']

        event_name = 'Event 1'
        expected_output = 'Event 1: Time 1'

        self.assertEqual(swimmer.lookup_event(event_name), expected_output)

    def test_lookup_event_not_found(self):
        swimmer = Swimmer("http://www.example.com")
        swimmer.event_list = ['Event 1: Time 1', 'Event 2: Time 2']

        event_name = 'Event 3'
        expected_output = 'Event 3 not found'

        self.assertEqual(swimmer.lookup_event(event_name), expected_output)

    def test_get_event_with_no_rows(self):
        swimmer = Swimmer("http://www.example.com")
        html_doc = '<html><body><table id="js-swimmer-profile-times-container"></table></body></html>'
        soup = BeautifulSoup(html_doc, 'html.parser')

        expected_output = []
        self.assertEqual(swimmer.get_event(soup), expected_output)

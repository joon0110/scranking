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

    def test_get_name_with_valid_input(self):
        html_doc = '<html><head><title>Sample Title | Swimcloud</title></head></html>'
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Call the function and check the output
        self.assertEqual(swimmer.get_name(soup), "Sample Title")

    @patch('requests.get')
    def test_get_info(self, mock_get):
        swimmer = Swimmer("http://www.example.com")
        mock_response = MagicMock()
        html = "<html><body><ul><li>Hometown</li><li>University: <a>University</a></li></ul>" \
               "<div class='btn-icon-plain'><a href='http://twitter.com'>Twitter</a></div>" \
               "<div class='btn-icon-plain'><a href='http://instagram.com'>Instagram</a></div>" \
               "<div class='btn-icon-plain'><a href='http://facebook.com'>Facebook</a></div></body></html>"
        swimmer.get_info(html)
        self.assertEqual(swimmer.get_info(soup), "University Twitter Instagram Facebook")


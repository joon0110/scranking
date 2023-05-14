# scranking

scranking is a python library that display ranking of the college swimmer

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![GitHub issues](https://img.shields.io/github/issues/joon0110/scranking)
[![Build Status](https://github.com/joon0110/scranking/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/joon0110/scranking/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/joon0110/scranking/branch/main/graph/badge.svg)](https://codecov.io/gh/joon0110/scranking)
[![PyPI](https://img.shields.io/pypi/v/scranking)](https://pypi.org/project/scranking/)
[![Docs](https://readthedocs.org/projects/scranking/badge/?version=latest)](https://scranking.readthedocs.io/en/latest/)

## Overview

Scranking is a library that scrapes data from a website such as [swimcloud](https://www.swimcloud.com/swimmer/549377/), which is website that shows times and ranking of the college swimmer. 

The library will allow users to simpily type the URL and get all the neccessary information of that swimmer.

## Install

Install using 'pip install scranking' in the command line.

## Quickstart of scranking

```python
from scranking import Swimmer

    # Initialize the swimmer object with your swimcloud url
    swimmer = Swimmer("url")

    # Check if the browser is working
    swimmer.get_http_status()

    # Create a bf4 for that swimmer objecft
    swimmer.get_soup()

    # Save the html of the website into text file
    swimmer.save_soup_to_file("soup", "filename.txt")

    # Get the full name of that swimmer with the soup you created
    swimmer.get_name("soup")

    # Find a line html that contains swimmer's social network information and hometown
    swimmer.get_info("infohtml")

    # Get all the events for that swimmer with the best time
    swimmer.get_event("soup")

    # A search method for get_event method
    swimmer.lookup_event("40 L Free")
```
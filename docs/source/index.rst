.. scranking documentation master file, created by
   sphinx-quickstart on Sun Apr  9 16:09:46 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to scranking's documentation!
=====================================

.. contents::
    :depth: 1


Installation
============

To install "scranking" open up any terminal you prefer and run the following command:

.. code-block:: console

    pip install scranking


This commnad will download the latest version of "scranking" and its dependencies. Once the installation is complete, you can import "scranking" and use it on you python project.

Note: If you do not install "scranking" and run its function, it will throw an error.

Quickstart of scranking
=======================

.. code-block:: Python

    from scranking import Swimmer

    # Initialize the swimmer object with your swimcloud url
    swimmer = Swimmer("url")

    # Check if the browser is working
    swimmer.get_http_status()

    # Create a bf4 for that swimmer objecft
    swimmer.get_soup()

    # Get the full name of that swimmer with the soup you created
    swimmer.get_name(soup)

    # Find a line html that contains swimmer's social network information
    swimmer.get_info(infohtml)

API Docs
========

.. toctree::
    :maxdepth: 1

    modules/swimmer
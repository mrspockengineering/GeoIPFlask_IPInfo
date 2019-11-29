Geolocation_ipinfo
==================

The simplest GeoIP lookup library for Flask.

.. image:: https://raw.githubusercontent.com/whois-api-llc/flask-simple-geoip/master/images/geoip.png

.. image:: https://img.shields.io/travis/whois-api-llc/flask-simple-geoip.svg
    :alt: flask-simple-geoip Build
    :target: https://travis-ci.org/whois-api-llc/flask-simple-geoip


This simple Flask application shows GeoIP information
Functionalities:
- shows external IP
- shows GeoIP information for requested IPs, like:
- no registration needed

Meta
----
- Author: Markus Gradl
- Email: mrspock.munich@gmail.com
- Twitter: -
- Site: -
- Status: production ready


Prerequisites
-------------

no prerequisities needed


Installation
------------

To install `Geolocation_ipinfo` using `pypi <https://pypi.org/>`_, simply run:

####
.. code-block:: console

    $ pip install flask-simple-geoip

In the root of your project directory.


Usage
-----

Once you have `flask-simple-geoip` installed, you can use it to easily find the
physical location of a given IP address.

This library gives you access to all sorts of geographical location data that
you can use in your application in any number of ways.

Here's a simple Flask app that makes use of the geolocation lookups:

.. code-block:: python

    from flask import Flask, jsonify
    from flask_simple_geoip import SimpleGeoIP


    app = Flask(__name__)

    # Initialize the extension
    simple_geoip = SimpleGeoIP(app)


    @app.route('/')
    def test():
        # Retrieve geoip data for the given requester
        geoip_data = simple_geoip.get_geoip_data()

        return jsonify(data=geoip_data)

Here's the sort of data you might get back when performing a geoip lookup
request:    
    
Details:
	{
		'ip': '8.8.8.8',
		'hostname': 'dns.google',
		'city': 'Mountain View',
		'region': 'California',
		'country': 'US',
		'loc': '37.3860,-122.0838',
		'org': 'AS15169 Google LLC',
		'postal': '94035',
		'timezone': 'America/Los_Angeles',
		'country_name': 'United States',
		'latitude': '37.3860',
		'longitude': '-122.0838'
	}
	
By default, this library handles retrying failed HTTP requests for you. For
instance: if the GeoIPify API service is currently down or having issues,
your request will be retried up to three consecutive times before failing.

In the event a geoip lookup still can't return successfully, the data returned
will be `None`. This library will *never* throw an exception. This decision was
made strategically: not having geoip data should never be the cause of a failed
request. =)

Comparison to other GeoIP libraries
-----------------------------------
flask-simple-geoip


Changelog
---------

All library changes in descending order.


Version 0.1.1
*************
hallo


Version 0.1.0
*************

**Released Nov 19, 2019**

- First release!

'''
Created on 26.11.2019

https://www.whoisxmlapi.com/blog/how-to-perform-a-geoip-lookup-in-flask/?fbclid=IwAR3ZipeA6jlZuV1RRdtobPpkKu7FCAvoz_26Xt3gxj3wqaB1LmqVu37zFxc

version 0.1.0

@author: Markus Gradl
'''
from flask import Flask, jsonify, make_response
from GeoIP_flask_ipinfo import GeoIPFlaskIpinfo

from json import dumps

app = Flask(__name__)
app.config["GEOIPFY_API"] = 'https://api.ipify.org'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# simple_geoip = SimpleGeoIP(app)
simple_geoip_object = GeoIPFlaskIpinfo()

def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response

@app.route("/myIP")
def GeoIP_myIP():
    my_public_ip = simple_geoip_object.get_my_public_IP()
    geoip_data = simple_geoip_object.get_geoIP(my_public_ip)
    return jsonify(**geoip_data)

@app.route('/publicIP/<string:ip_address>')
def GeoIP_IP_pub(ip_address):
    print(ip_address)
    geoip_data=simple_geoip_object.get_geoIP(ip_address)
    return jsonify(data = geoip_data, indent=2)  # pretty json


@app.route("/hello")
def hello():
    return "hello, world!"

if __name__ == "__main__":
    app.run()
'''
Created on 25.11.2019

Goal:
zu best. IP GeoInfo:
- Firma
- city

Sample Output:

APIs:
https://ipinfo.io/developers

whois domain -> IP:
http://whois.domaintools.com/heise.de

version 0.1.0

@author: Markus Gradl
'''
import ipinfo
import requests

access_token = 'ipinfo.io'  #'123456789abc'
handler = ipinfo.getHandler(access_token)

class GeoIPFlaskIpinfo(object):
    def get_geoIP(self, ip_address):        
        try:
            details = handler.getDetails(ip_address)
        except:
            details =  None
        return details.all
    
    def get_my_public_IP(self):
        try:
            my_public_ip = requests.get('https://api.ipify.org').text
        except:
            my_public_ip = None
        return my_public_ip
        
# test data    
ip_address =    '8.8.8.8'       #'54.176.0.0'
    # '8.8.8.8' : Google
    # '54.183.142.105' : Amazon.com    weitere Amazon.com: '54.176.0.0' - '54.191.255.255',     13.224.9.115
    # '193.99.145.37' : heise.de
    # '192.109.190.2'  : bmw.de
    # '159.51.236.21    : schaeffler;     62.48.81.20: Schaeffler.com
    # '81.169.145.159'    : botmaniacs.de
    # eigene: '2.206.8.105'  #   
    
ip_address2 = '8.8.8.8'# '62.48.81.20'
# 

# print('My public IP address is', my_public_ip)

details = handler.getDetails(ip_address); details2 = handler.getDetails(ip_address2)
# # details_publicIP = handler.getDetails(my_public_ip)
print("City :", details.city)
# 'Mountain View'
print(details.loc)
print("Company: ",details.org)
print("company 2: ", details2.org)
# '37.3861,-122.0840'
print("Details: ", details2.all)
# print('Details MyIP:', details_publicIP.all)

response = requests.get('http://ipinfo.io/'+ip_address2+'/city')
# response = requests.get('http://ipinfo.io/'+ip_address2+'/company')
print(response.content)

# requests.get("www.heise.de", params)


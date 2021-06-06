from socket import timeout
import requests
import Constants
import time

def IsSiteOnline (siteUrl):
    response = requests.get(siteUrl)
    if (response.status_code==200):
        return True
    else:
        return False

if(IsSiteOnline(Constants.BASE_URL)==True):
    print("Website je online")
else:
    print("website nije online")


timeout(10)

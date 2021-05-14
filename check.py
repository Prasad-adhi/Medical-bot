import requests

def checkblock(url):
    r = requests.get(url)
    print(r.status_code)

url="https://www.everydayhealth.com/diarrhea/treatment/dos-donts-treating-diarrhea-quick-relief/"
checkblock(url)
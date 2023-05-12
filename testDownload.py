import requests

url = 'https://m-selig.ae.illinois.edu/ads/coord_seligFmt/2032c.dat'
r = requests.get(url, allow_redirects=True)

open('2032c.dat', 'wb').write(r.content)
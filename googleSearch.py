import urllib , urllib3 , json
query = input("What are you want to search for?\n >>")
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
query = urllib.urlencode( {'q' : query } )
response = urllib3.urlopen (url + query ).read()
data = json.loads ( response )
results = data [ 'responseData' ] [ 'results' ]

for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )
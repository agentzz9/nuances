import urllib2
import re
import requests

url = 'http://www.imdb.com/chart/top'

#http://www.omdbapi.com/?i=tt0246578&plot=full&r=json
omdb_url = 'http://www.omdbapi.com'

response = urllib2.urlopen(url)
imdbhtml = response.read()

imdbids_href = re.findall(r'<a href="/title/\w+', imdbhtml)
imdbids_href = list(set(imdbids_href))


# <a href="/title/tt2267998

imdbids = [  s[16:] for s in imdbids_href  ]
#print(imdbids)
#print(len(imdbids))

csv_ids = ','.join(imdbids)

#print(csv_ids)

#put in file for future ref. no particular reason
f = open('imdbids.txt','w')
f.write(csv_ids)
f.close()

f = open('imdb250s.txt','w')

jsons = []
count = 0
for imdb_id in imdbids:
    print(count)
    count+=1
    payload = {'i': imdb_id, 'plot': 'full', 'r':'json'}
    r = requests.get(omdb_url, params=payload)
    jsons.append(r.text.encode('UTF-8'))
    #this^ was a pain finding out, write was causing issues
    
    
#print(jsons)

f.write('\n'.join(jsons))
f.close()

print("done")



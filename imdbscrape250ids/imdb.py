import urllib2
import re

url = 'http://www.imdb.com/chart/top'


response = urllib2.urlopen(url)
imdbhtml = response.read()



imdbids_href = re.findall(r'<a href="/title/\w+', imdbhtml)
imdbids_href = list(set(imdbids_href))


# <a href="/title/tt2267998

imdbids = [  s[16:] for s in imdbids_href  ]
print(imdbids)
print(len(imdbids))

csv_ids = ','.join(imdbids)

print(csv_ids)

f = open('imdbids.txt','w')
f.write(csv_ids)

f.close()

print("done")



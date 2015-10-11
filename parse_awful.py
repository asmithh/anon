with open('the_worst.txt') as f:
	content = []
	for line in f.readlines():
		content.append(line)
	f.close()
lines = []
import re
for i in content:
	for j in  re.split( 'time', i):
		if len(j) > 3:
			lines.append(j)
edits = []
k = 0
while k < len(lines):
	t = lines[k]
	#print t
	#print t[:-1]
	t = t[:-1].split()
	#print t
	e = lines[k + 1]
	k = k+2
	time = {'day_of_week': t[0], 'hour' : t[1], 'minute' : t[2], 'second' : t[3]}
	#print e
	#print time
	httpsplit =  re.split('http', e)
	title = httpsplit[0]
	editurl = 'Null'
	#print httpsplit
	try:
		articleurl = 'http' + httpsplit[1]
		
		#print httpsplit[2].split(' ', 1)
		articleurl = 'http' + httpsplit[1]
		editurl = 'http' + httpsplit[2].split(' ', 1)[0]
		#print editurl
		rest_of = httpsplit[2].split(' ', 1)[1]
	except:
		try:
			articleurl = 'http' + httpsplit[1].split(' ', 1)[0]
			rest_of = httpsplit[1].split(' ', 1)[1]
		except:
			pass
	#print rest_of
	editdelta = re.findall('\-*[0-9]+', rest_of)
	#print editdelta
	#print articleurl
	whatlang = re.findall('[A-Za-z]+ Wikipedia', rest_of)
	#print whatlang
	newPage = 'true' in rest_of
	e = {'editurl' : editurl, 'editdelta' : editdelta, 'articleurl' : articleurl, 'whatlang' : whatlang, 'newpage' : newPage, 'title' : title}
	edits.append((time, e))

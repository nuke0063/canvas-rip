import canvaslms.api as api
import os
import urllib.request
authToken = api.getAuthTokenFromFile('./KEY')
apiObj = api.CanvasAPI('someschool.instructure.com', authToken) #Define url as school.instructure.com
results = apiObj.allPages('courses/')
for i in results:
	directory = i['course_code'].replace(" ","")
	if not os.path.exists(directory):
		os.makedirs(directory)
		classid = i['id']
		if classid == 14262: # Define classes that do not have any files. It will give urllib errors when it hits the class if not
			continue
		if classid == 165941: # More class defines
			continue
		if classid == 56779: #...more class defines
			continue
		print('For class: ' + str(classid))
		classfiledir = apiObj.allPages('courses/'+str(classid)+'/files')
		for j in classfiledir:
			if(os.path.exists(str(directory + '/' + j['filename'].replace("+","")))):
					print('Already have: ' + str(j['filename']) + ' for ' + str(i['course_code'].replace(" ","")))
			else:
					print('Grabbing : ' + str(j['filename']) + ' for ' + str(i['course_code'].replace(" ","")))
					urllib.request.urlretrieve(str(j['url']),str(directory + '/' + j['filename'].replace("+","")))
print('Done.')


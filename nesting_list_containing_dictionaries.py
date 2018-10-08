# nesting
# list containing dictionaries
'''
s = {'name' : 'somesh', 'age' : '17 years'}
a = {'name' : 'aakash' , 'age' :'21 years' }
sa = [s,a]
for i in sa :
    for j , k in i.items():
        print('\n' + 'users ' + str(j) + ' is ' + str(k))
        '''

#nesting
# dictionaries containing lists
'''
fav_movies = {
    'somesh' : ['infinity war', 'Jobs' , 'The Social Network'],
    'aakash' : ['pokemon' , 'Avengers' ,'Doraemon']
    }
for i , j in fav_movies.items():
    print('\n' + str(i)  +" 's " + 'favourite movies are' )
    for names in j :
        print('\t' + str(names))
'''
#nesting
#dictionaries containing dictionaries
d = {
    "somesh" : {'age' : '17 years' , 'e-mail' : 'someshkalyankar@gmail.com'},
    "aakash" : {'age' : '21 years' , 'e-mail' : 'aakashdk0109@gmail.com'}
    }
for names , about in d.items():
    print('\n' + 'username : '+ str(names))
    for key , value in about.items():
        print('\t' + str(key) + ' : ' + str(value))

x = [('hii', 'noun'), ('good', 'noun'),('good', 'noun'), ('run', 'verb'), ('bad', 'adj'),
     ('good', 'noun')]
countgood = 0
countbad = 0
for i,j in x:
    if i=='good' and j=='adj':
        countgood = countgood + 1
    elif i == 'bad' and j == 'adj':
        countbad = countbad+1
    else:
        pass

if countgood > countbad:
    print('sentiment is positive')
elif countgood < countbad:
    print('sentiment is negetive')
else:

    print('sentiment is neutral')
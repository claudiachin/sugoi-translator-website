import csv

with open('sugoi-translator-website/static/feature3.csv', newline='') as csvfile:
    result = ''
    r=0

    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        res = '<tr>\n'
        for item in row:
            if '\\' in item:
                newItem = '{@html "'+item+'"}'
            else:
                newItem = item
            
            if r==0:
                res += '<th><h6>'+newItem+'</h6></th>\n'
            else:
                res += '<td><p>'+newItem+'</p></td>\n'

        r = 1
        res += '</tr>\n'
        result += res
    
    print(result)
"""
    Name: Bryant Hanks
    Assignment: CS336 Assignment #7
    Created: 11/20/2022
    Description: pythonscript
 """
import os

regList = []
htmlList = []


try:
    with open('nametags10.html', 'r+') as htmlFile:
        for line in htmlFile.readlines():
            htmlList.append(line)
            htmlFile.close()
except:
    print("Error opening HTML file")

try:
    with open('registrant_data.csv', 'r') as regFile:
        for line in regFile:
            lineList2 = line.split(sep=',')
            regDict = {
                'date': lineList2[0],
                'title': lineList2[1],
                'fName': lineList2[2],
                'lName': lineList2[3],
                'addy1': lineList2[4],
                'addy2': lineList2[5],
                'city': lineList2[6],
                'state': lineList2[7],
                'zip': lineList2[8],
                'tele': lineList2[9],
                'email': lineList2[10],
                'position': lineList2[11],
                'company': lineList2[12],
                's1': lineList2[13],
                's2': lineList2[14],
                's3': lineList2[15]
            }

            regList.append(regDict)


except:
    print("error opening registrant file")

registrantLength = len(regList)
ppl = len(regList) - 1

os.chdir("..")

f = open(os.path.abspath(os.curdir) + '\\nametags10gen.html', 'w')
for i in range(0, 21):
    f.write(htmlList[i])

for i in range(1, ppl + 1):
    #determine if page break is needed
    if (i % 10 == 1) and (i != 1):
        #f.write('<!-- ' + str(i) + ' first if -->\n') #troubleshooting
        f.write('    </div>\n')
        f.write('    <div class ="page">\n')
        f.write('        <div class="row">\n')
        f.write('            <div class="nameTag"><p>' + regList[i]['fName'] + ' ' + regList[i]['lName'] + \
                '</p><p>' + regList[i]['position'] + '</p><p>' + regList[i]['company'] + \
                '</p><p>' + regList[i]['city'] + ', ' + regList[i]['state'] + '</p></div>\n')

    #if it's the last person and it's an odd number of people
    elif (i == ppl) and (i % 2 > 0):
        f.write('<!-- ' + str(i) + ' second if -->\n') #troubleshooting
        f.write('        <div class="row">\n')
        f.write('            <div class="nameTag"><p>' + regList[i]['fName'] + ' ' + regList[i]['lName'] + \
                '</p><p>' + regList[i]['position'] + '</p><p>' + regList[i]['company'] + \
                '</p><p>' + regList[i]['city'] + ', ' + regList[i]['state'] + '</p></div>\n')
        f.write('            <div class="nameTag"><p></p><p></p><p></p><p></p></div>\n')
        f.write('        </div>\n')

    #if odd number we're on the first column
    elif i % 2 > 0:
        #f.write('<!-- ' + str(i) + ' third if ' + str(ppl) + ' -->\n') #troubleshooting
        f.write('        <div class="row">\n')
        f.write('            <div class="nameTag"><p>' + regList[i]['fName'] + ' ' + regList[i]['lName'] + \
                '</p><p>' + regList[i]['position'] + '</p><p>' + regList[i]['company'] + \
                '</p><p>' + regList[i]['city'] + ', ' + regList[i]['state'] + '</p></div>\n')

    #second column and if it's the last person close up divs
    else:
        #f.write('<!-- else' + str(i) + ' ' + str(ppl) + '-->\n') #troubleshooting
        f.write('            <div class="nameTag"><p>' + regList[i]['fName'] + ' ' + regList[i]['lName'] + \
                '</p><p>' + regList[i]['position'] + '</p><p>' + regList[i]['company'] + \
                '</p><p>' + regList[i]['city'] + ', ' + regList[i]['state'] + '</p></div>\n')
        f.write('        </div>\n')

f.write('    </div>\n')
f.write('</body>\n</html>')

f.close()

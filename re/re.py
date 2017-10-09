import re
#####
f1 = re.compile('(\S\S)\S*')
print(f1.sub('\g<1>',"Earth is the third planet from the Sun"))

#####
f2 = re.compile('\S*@(\S*[.]\S*)')
print(f2.sub('\g<1>','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'))

#####
f3 = re.compile('\S* \d*-\d* (\d{2})-(\d{2})-(\d{4})')
print(f3.sub('Year: \g<3> Month: \g<1> Day: \g<2>','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'))

#####
temp = (re.findall('\s[aeiou]\S*|[AEIOU]\S*',"Earth's gravity interacts with other objects in space, especially the Sun and the Moon."))
print([i.strip() for i in temp])

#####
lst= ['010-256-1354', '010-1234-5576', '070-642-0384', '010-290*-4858','0105734123']

f5 = re.compile('010-\d{3,4}-\d{4}')

for i in lst:
    if f5.match(i) != None and len(f5.match(i)[0]) < 14:
        print(True)
    else : print(False)

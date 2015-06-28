import re
#https://www.youtube.com/watch?v=sZyAn2TW7GY

'''
START REGEX:
    line1 = '   prices re/ 324234 '

    regex = re.findall(r'yourRegExpression',line1)
    print regex

identifiers:
    \d{1,6}\s = finds first 6 numbers and stop searching when whitespace
    \d{1,6} = finds first 6 numbers

    \d = any number
    \D = anything but a number
    \s = space
    \S = anything but a space
    \w = letters
    \W = anything but letters
    . = any character except for new line
    \b = word1 word2 word3
    \.

Modifiers:
    \d(1,5) 44,545, 55555, 45242421
    + = matches 1 or more
    ? = matches 0 or 1
    = 0 or more
    $ match end for a string
    ^ match start of the string
    {x} = this amount of preceding code

WHITER SPACE CHARACTER:
    \n = new line
    \s = space
    \t = tab
    \e = escape
    \r = carriage return
    \f = form feed

ESCAPE REQUIRED:
    , + * ? [] $ ^ () \

    SAMPLE CODE1 REGEX:
    line1 = '   prices re/ 324234 '


    regex = re.findall(r'\d{1,6}',line1)

    print(regex)


    '''
    
#########################################
#START REGEX SAMPLE CODE WITH DICTIONARY

#VARIABLES
exampleString = 'Jessica is 17 , and Jane is 18'

ages = re.findall(r'\d{1,3}'  , exampleString)
names = re.findall(r'[A-Z][a-z]*' , exampleString)

#PRINT STATEMENTS
print(ages)
print(names)

# FOR LOOP
ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1


#  <sampleDict>
# 1 level dictionary
exDict1 = {'Jack:16,Jones:17,Jason:18'}
print(exDict1)
#  2 levels dictionary
exDict2 = {'Jack':[16,'blonde'], 'Bob':[22,'brown'], 'Alice':[26,'black'],'Jane':[27,'red']}

#  print all values in Alice
print(exDict2['Alice'])
#  print level 2 value in Alice
print(exDict2['Alice'][1])

#  add to dictionary
exDict2['Jessica'] = 27

# delete from dictionary
del exDict2['Jessica']

#PRINT STATEMENTS FOR DICTIONARIES
print(exDict2)

#  </sampleDict>


print(ageDict.keys)

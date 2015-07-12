#http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

tu = (12,45,22222,103,6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)

#Prints out:
# 12 22222 45 22222 103 22222 6 22222

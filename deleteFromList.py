#https://www.daniweb.com/software-development/python/threads/68765/how-to-remove-a-number-of-lines-from-a-text-file-
""" assume part of your list1.txt data file looks like this:
1846440556
1846440521
1846440491
1846440505
1846441137
1846441102
1846441080
1846441331
1846441323
1846441315
"""
# read the data file in as a list
fin = open( 'list1.txt', "r" )
data_list = fin.readlines()
fin.close()
# test first 5 list items ...
print data_list[:5]
print '-'*60
# remove list items from index 3 to 5 (inclusive)
del data_list[3:5+1]
# test first 5 list items ...
print data_list[:5]
# write the changed data (list) to a file
fout = open("list2.txt", "w")
fout.writelines(data_list)
fout.close()

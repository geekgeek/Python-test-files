#combining lists in a dictionary

#converting txt to list
symbolfile = open("namesNordnet.txt")
symbolslist = symbolfile.read()
nameslist = symbolslist.split("\n")

#converting txt to list
linksfile = open("foo.txt")
linkslist = linksfile.read()
linkslist = linkslist.split("\n")

#combining 2 lists
comblist = dict(zip(nameslist, linkslist))
#mergedlist = list(set(linkslist + nameslist))


#<write combined list to txt file>
fo = open("nsymboljoin.txt", "w")
#</>

#loop
for keys,values in comblist.items():
    print(keys,values)
    #<write list to file>
    fo.write(keys+'\n'+values+'\n')
    #</>
    


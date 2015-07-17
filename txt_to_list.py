# http://stackoverflow.com/questions/8205807/how-to-convert-a-text-file-into-a-list-in-python
# convert txt file contents to list

#Read txt file:
symbolfile = open("C:\\codepython27\\pyfile.txt", "r")

yourResult = [line.split("\n") for line in symbolfile.readlines()]

print yourResult[:]

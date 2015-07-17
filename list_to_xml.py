#Converts lists to xml files
import xml.etree.cElementTree as ET

students = [1,2]
assignments=[100,101,102]
scores=[0,4,10]
results = ET.Element("results")
result = ET.SubElement(results,"result")
student = ET.SubElement(result,"student")
assignment = ET.SubElement(result,"assignment")
score = ET.SubElement(result,"score")

for s in students:    
    for a in range(len(assignments)):
        student.text = str(s)
        assignment.text = str(assignments[a])
        score.text = str(scores[a])
        results.append(result)
tree = ET.ElementTree(results)
tree.write('test.xml')

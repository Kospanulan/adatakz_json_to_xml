import json
import xml.etree.cElementTree as et

with open("test_json_file.json") as js:
    data = json.load(js)

root = et.Element("Employee")

et.SubElement(root, "fullname").text = data["fullname"]

ch = et.SubElement(root, "characteristics")
x = data["characteristics"]
for elem in x:
    # print(elem)
    et.SubElement(ch, elem).text = str(x[elem])

et.SubElement(root, "skills").text = str(data["skills"])

exp = et.SubElement(root, "experience")
for elem in data["experience"]:
        et.SubElement(exp, "position").text = elem["position"]
        et.SubElement(exp, "workplace").text = elem["workplace"]
        et.SubElement(exp, "salary").text = str(elem["salary"]) if "salary" in elem else ""
        et.SubElement(exp, "id_card").text = str(elem["id_card"]) if "id_card" in elem else ""
        et.SubElement(exp, "Country").text = elem["Country"] if "Country" in elem else ""


res = et.ElementTree(root)

res.write("test_xml.xml")

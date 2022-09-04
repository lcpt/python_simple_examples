import xml.dom.minidom


dom = xml.dom.minidom.parse('ugly_input_file.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
with open('pretty_output_file.xml', 'w') as os:
    os.write(pretty_xml_as_string)

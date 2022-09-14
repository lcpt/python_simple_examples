
import xml.dom.minidom
from dicttoxml import dicttoxml

array = [
    {
        'time': {"hour":"1", "minute":"30","seconds": "40"}
    },
    {
        'place': {"street":"40 something", "zip": "00000"}
    }
]

xml_string = dicttoxml(array, custom_root='test', attr_type=False)
dom = xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)

import xml.etree.cElementTree as ET
from xml.dom import minidom
import base64
import re


def format_poi(poi):
    html = ET.Element('html')
    head = ET.SubElement(html, 'head')
    style = ET.SubElement(head, 'style')
    body = ET.SubElement(html, 'body')
    style.text = """
    th,
    td,
    table{
      border: 1px solid black;
      border-collapse: collapse;
      text-align: center;

      table {
        border-left: 0px;
        border-right: 0px
      }  
    """
    content = ET.SubElement(body, 'table')
    if 'string' in poi.keys():
        format_string(poi, content)
    elif 'name' in poi.keys():
        format_func(poi, content)

    prettify(html)
    return prettify(html)


def format_string(poi, parent):
    head_row = ET.SubElement(parent, 'tr')
    for th in ['Data', 'Value']:
        col = ET.SubElement(head_row, 'th')
        col.text = th
    for item in poi.keys():
        if not item == '_id':
            row = ET.SubElement(parent, 'tr')
            data_style = ET.SubElement(row, 'td')
            val_style = ET.SubElement(row, 'td')
            data = ET.SubElement(data_style, 'strong')
            val = ET.SubElement(val_style, 'i')
            if item == 'string':
                poi[item] = poi[item].decode()
                print(base64_decode(str(poi[item])))
                val.text = base64_decode(str(poi[item])).decode()
            else:
                val.text = str(poi[item])
            data.text = item


def format_func(poi, parent):
    head_row = ET.SubElement(parent, 'tr')
    for th in ['Data', 'Value']:
        col = ET.SubElement(head_row, 'th')
        col.text = th
    for item in poi.keys():
        if not item == '_id':
            row = ET.SubElement(parent, 'tr')
            data_style = ET.SubElement(row, 'td')
            data = ET.SubElement(data_style, 'strong')
            if item == 'signature':
                val = ET.SubElement(row, 'table')
                format_signature(str(poi[item]), val)
            else:
                val_style = ET.SubElement(row, 'td')
                val = ET.SubElement(val_style, 'i')
                val.text = str(poi[item])
            data.text = item


def format_signature(sig, parent):
    variable = r'[_a-zA-Z]+[_\w]*'
    pattern = re.compile(r'([_a-zA-Z]+[_\w]*)\s(([_a-zA-Z]*[_\w]*\.)+[_a-zA-Z]+[_\w]*)\s(\(.*\))')
    match = pattern.search(sig)
    res = {'return_type': match.group(1), 'arguments': match.group(4)}

    head_row = ET.SubElement(parent, 'tr')
    for th in ['Data', 'Value']:
        col = ET.SubElement(head_row, 'th')
        col.text = th
    for item in res.keys():
        row = ET.SubElement(parent, 'tr')
        data_style = ET.SubElement(row, 'td')
        val_style = ET.SubElement(row, 'td')
        data = ET.SubElement(data_style, 'strong')
        val = ET.SubElement(val_style, 'i')
        val.text = str(res[item])
        data.text = item


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def base64_decode(base64_str):
    byte_str = base64_str.encode()
    decoded_str = base64.b64decode(byte_str)
    return decoded_str

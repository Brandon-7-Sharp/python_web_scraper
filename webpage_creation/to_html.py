from xml.etree import ElementTree as ET

txt_file = "info.txt"
html_file = "webpage.html"



#  Converts a text file with header and paragraph to an HTML file.
def txt_to_html(txt_file, html_file):
  lines = []

  with open(txt_file, 'r') as f:
    for line in f:
        lines.append(line)

    # Create root element for HTML, try to remember the structure of a HTML file
  root = ET.Element("html")

    # Create head and body elements, try to understand how subElements works
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "My News Aggregation Site"
  body = ET.SubElement(root, "body")

  content = []

  i=0

  for j in range(10):
    # Read text file content
    # print(i+1)
    content.append(lines[i])
    content.append(lines[i+1])

    # Extract header and paragraph, since you will be having multiple articles the logic will
    # change for the code given below. 
    header = content[0].strip()
    paragraphs = "".join(content[1:]).strip()

    # Create header and paragraph elements in body
    h1 = ET.SubElement(body, "h1")
    h1.text = header
    p = ET.SubElement(body, "p")
    p.text = paragraphs

    i+=2
    content = []

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')

txt_to_html(txt_file, html_file)
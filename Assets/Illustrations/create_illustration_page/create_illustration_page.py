import glob
from dominate import document
from dominate.tags import *
import sys
import os

# Script that creates an html file that displays all images of a specified folder.

# Styles could be supplied via styles.css file.
# -----------------------
# prerequisite: dominate
# pip install dominate OR pip install --no-cache-dir -r requirements.txt
# -----------------------

# Inputs:
# 1: input directory (folder containing images)
# 2: document title (header displayed on top)
# Output:
# index.html will be created next to the images - Keep file in there as paths in index.html are relative

scriptDirectory = os.path.dirname(os.path.realpath(__file__))
inputDirectory = os.path.join(scriptDirectory, "../")
documentTitle = "The Liberators Illustrations"

if len(sys.argv) == 4:
    print('Using custom input directory and document title')
    inputDirectory = sys.argv[1]
    documentTitle = sys.argv[3]

outputFile = os.path.join(inputDirectory, "index.html")
print('Input Directory: ', inputDirectory)
print('Output File: ', outputFile)
print('Document Title: ', documentTitle)

images = glob.glob(inputDirectory + '/*.png')

with document(title=documentTitle) as doc:
    h1(a(documentTitle, href="https://github.com/theliberators/usergroups/tree/main/Assets/Illustrations"))

    for path in images:
        span(img(src=os.path.basename(path), style="width:30%"), _class='photo')

with doc.head:
    link(rel='stylesheet', href='style.css')


with open(outputFile, 'w') as f:
    f.write(doc.render())
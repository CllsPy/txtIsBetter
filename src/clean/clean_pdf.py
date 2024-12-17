from load.load_pdf import loadPdf
import re

def cleanPDF(path):
    txt = loadPdf(path)
    strip_whitespace = txt.strip().lower()
    removed_ponct = strip_whitespace.replace(".", "")
    removed_regex = re.sub('[^A-Za-z0-9]+', ' ', removed_ponct)

    with open("file.txt", "w") as output:
        output.write(str(removed_regex))
 
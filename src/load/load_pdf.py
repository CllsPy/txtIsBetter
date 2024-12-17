def loadPdf(pdf):
    with open(pdf) as file:
        text = file.read()
    
    print(text)

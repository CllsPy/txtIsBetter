def loadPdf(pdf):
    with open(pdf) as file:
        txt = file.read()
    
    return txt

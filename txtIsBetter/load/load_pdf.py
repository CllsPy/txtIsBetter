def load_pdf(pdf):
    with open(pdf) as file:
        text = file.read()
    
    print(text)

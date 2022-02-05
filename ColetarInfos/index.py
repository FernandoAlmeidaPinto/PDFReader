from ReadPDF.pdfminer import ReadPDF
from ColetarInfos.Securitizadora import PegaSecuritizadora

def FuxoLeituraPDF(path):

    text = ReadPDF().convert_pdf_to_txt(path)
    securitizadora = PegaSecuritizadora(text)
    return { "Securitizadora": securitizadora}
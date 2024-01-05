from PyPDF2 import PdfReader

class PDFReader:
    
    def get_text(self,file:str)->str:
        pdfreader = PdfReader(file)
        # read text from pdf
        
        temp = ''
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                temp += content
        
        return temp
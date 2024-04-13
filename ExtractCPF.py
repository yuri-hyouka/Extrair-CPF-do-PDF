from PyPDF2 import PdfFileReader
import os
import shutil
import re  

diretorio = '/entrada'
diretorio_destino = '/saida'

#percorre todos pdfs do diretorio
for filename in os.listdir(diretorio):
    if filename.endswith('.pdf'):
        filepath = os.path.join(diretorio, filename)
        
        #expressão regular para busca de CPF
        cpf_pattern = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"

        # Abrindo um arquivo PDF existente
        with open(filepath, "rb") as input_pdf:
            # Criando um objeto PdfFileReader
            pdf_reader = PdfFileReader(input_pdf)

            # Obtendo o número de páginas do arquivo PDF
            num_pages = pdf_reader.numPages
            # Lendo o texto de cada página
            for page_number in range(num_pages):
                page = pdf_reader.getPage(page_number)
                text = page.extractText()
                cpfs_encontrados = re.findall(cpf_pattern, text)

                for cpf in cpfs_encontrados:
                    cpf_convertido = cpf.replace('.', '').replace('-', '')

                caminho_convertido = "arquivos/" + cpf_convertido + ".pdf"
                output = os.path.join(diretorio_destino,caminho_convertido)
                shutil.move(filepath, output)
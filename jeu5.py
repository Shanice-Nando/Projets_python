#le module filecmp permet de comparer deux fichiers par leurs octets.
import filecmp
def pdf_identiques(chemin_pdf1,chemin_pdf2):
     return filecmp.cmp(chemin_pdf1,chemin_pdf2)
pdf1= "C:\\Users\\tojir\\Documents\\HTML.pdf"
pdf2= r"C:\Users\tojir\Documents\HTML.pdf"
if pdf_identiques(pdf1,pdf2):
    print("Les deux fichiers PDF sont identiques.")
else:
    print("Les deux fichiers PDF sont différents.")
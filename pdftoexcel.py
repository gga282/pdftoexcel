#
import pandas as pd
import pdfplumber
import os,sys
import glob
import questionary


files_folder=glob.glob('PDFs/*.pdf')
if not files_folder:
    print("No pdf files available")
    print("Quiting....")
    sys.exit(0)
else:
    select_pdf=questionary.select("Please select pdf file: ",choices=files_folder+['Exit']).ask()

pdf=pdfplumber.open(select_pdf)
pages_to_read=pdf.pages


im=[]

table_settings={
    "vertical_strategy":"lines",
    "horizontal_strategy":"text",
    "snap_y_tolerance":5,
    "intersection_x_tolerance":15,
}

table=[]

for page in pages_to_read:
    extracted_table=page.extract_table(table_settings)
    if extracted_table:
        table.extend(extracted_table)

col=table[0]  

excel_file=pd.DataFrame(table,columns=col)
excel_file.to_excel('deneme.xlsx')

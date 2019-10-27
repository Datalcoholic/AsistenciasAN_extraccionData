import camelot
import os
import pandas as pd

pd.options.display.max_columns = None


# TODO:
# Converitn en funcion

def extract_tables(url, fileName):
    pass
    filePath = 'c://Users/Pt/Documents/python/Proyectos/Asistencias_AN/PDF/listado-de-asistencias-de-los-diputados-y-diputadas-a-la-asamblea-nacional-correspondiente-al-mes-de-junio-de-2019-245.pdf'

    tables = camelot.read_pdf(filePath, pages='1-end')

    tablesN = len(tables)
    master = []

    for t in range(0, tablesN):

        rep = (tables[t].parsing_report)
        print(
            f"Extrayendo tabla Nº {rep['order']} de la pagina Nº{rep['page']} con exactitud del {rep['accuracy']} y espacio blanco del {rep['whitespace']}\n")

        master.append(tables[t].df)

    result = pd.concat(master)
    result.to_excel('asistencias.xlsx')

import tabula, os

tabula.convert_into_by_batch(os.getcwd(), output_format='csv', pages='all')
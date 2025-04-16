import pandas as pd

def load_file_to_dict(path):
    xls = pd.ExcelFile(path)
    return {
        sheet_name: xls.parse(sheet_name).to_dict(orient="records")
        for sheet_name in xls.sheet_names
    }
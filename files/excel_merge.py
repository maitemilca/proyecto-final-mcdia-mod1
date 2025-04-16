import pandas as pd

def merge_excels(path_list, path_out, sheet='Metadata'):
    """
    Une múltiples archivos Excel en un solo archivo.

    :param path_list: Lista de rutas de archivos Excel.
    :param path_out: ruta del archivo Excel combinado.
    :param hoja: Nombre de la hoja de salida.
    """
    dataframes = []
    for path in path_list:
        print (path)
        df = pd.read_excel(path)
        df['ARCHIVO_ORIGEN'] = path  # Agrega el nombre del archivo como referencia
        dataframes.append(df)

    df_combinado = pd.concat(dataframes, ignore_index=True)
    df_combinado.to_excel(path_out, index=False, sheet_name=sheet)
    print(f" Archivos combinados correctamente en: {path_out}")

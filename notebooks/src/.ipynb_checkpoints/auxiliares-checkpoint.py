import pandas as pd


def dataframe_coeficientes(coefs, colunas):
    return pd.DataFrame(data=coefs.ravel(), index=colunas, columns=["coeficiente"]).sort_values(
        by="coeficiente"
    )

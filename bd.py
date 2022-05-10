import pathlib
import pandas as pd

def viajes():
    PATH = pathlib.Path(__file__).parent
    PATH_FOLDER=PATH.joinpath('../datasets').resolve()
    ruta = PATH_FOLDER.joinpath('viajes.csv')
    df = pd.read_csv(ruta)
    df['cantidad']=1
    sector = df.groupby(['sector'])['cantidad'].sum().reset_index(name='cantidad')
    origen = df.groupby(['origen'])['cantidad'].sum().reset_index(name='cantidad')    
    return df,sector,origen

def empresasTech():
    PATH = pathlib.Path(__file__).parent
    PATH_FOLDER = PATH.joinpath('../datasets').resolve()
    ruta=PATH_FOLDER.joinpath('empresasTech.csv')

    df = pd.read_csv(ruta)
    df = df.rename(columns={'TIPO_TRANSPORTE':'transporte'})
    tipoTransporte = df.groupby(['transporte'])['CANTIDAD'].sum().reset_index(name='cantidad')

    return df,tipoTransporte
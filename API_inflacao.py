import pandas as pd
import numpy as np

def API_busca_inflacao():
    periodos ='https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/'
    iris = pd.read_json(periodos)

    # Busca dos meses
    meses = []
    for mes in iris["id"]:
        meses.append(mes)
    
    # Busca dos links
    links = []
    for mes in meses:
        link_string = "https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/" + str(mes) + "/variaveis/63|69|2265?localidades=N1[all]&classificacao=315[7169]"
        links.append(link_string)
    
    # Busca do nome das colunas
    buscanome = pd.read_json("https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/202001/variaveis/63|69|2265?localidades=N1[all]&classificacao=315[7169]")
    d = buscanome["variavel"]
    colunas=[]
    colunas.append(d[0]), colunas.append(d[1]), colunas.append(d[2])


    df = []

    lista_aux = []
    
    for link in links:
        lista_atual = []

        a = pd.read_json(link)

        for coluna in range(0,3):
            aux = str(a["resultados"][coluna])
            index = aux.find("'serie': {")
            b = aux[index:-6]
            try:
                c = float(b[21:])
                lista_atual.append(c)
            except:
                lista_atual.append(np.nan)

        lista_aux.append(lista_atual)
        
    
    novodf = pd.DataFrame(columns=colunas, index=meses, data=lista_aux)

    return novodf.to_excel("Resultado_Valores.xlsx")


API_busca_inflacao()
import requests
import pandas as pd

meses = ['01 - Janeiro', '02 - Fevereiro', '03 - Março', '04 - Abril', '05 - Maio', '06 - Junho', '07 - Julho', '08 - Agosto', '09 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']

a = 2020
m = 3

def DadoBruto(a, m, meses):
    mes = meses[m-1].replace(' ', '%20')
    ano = a
    urlBase = 'https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20opera%C3%A7%C3%B5es%20a%C3%A9reas/Voo%20Regular%20Ativo%20%28VRA%29/'
    response = requests.get(urlBase)
    response.encoding = "utf-8-sig"
    df = pd.read_json(response.json)

DadoBruto(a, m, meses)
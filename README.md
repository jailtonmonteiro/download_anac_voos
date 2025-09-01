# 📊 Download de Dados de Voos da ANAC  

## 📌 Objetivo  
O objetivo deste projeto é realizar o download e disponibilização do histórico de voos, dados públicos fornecidos pela [ANAC](https://www.gov.br/anac/pt-br) em formato **CSV**.  

Esses dados podem ser utilizados em estudos de **ciência de dados, estatística, análise de transporte aéreo** e visualizações.  

---

## 📂 Estrutura do Projeto  
```
├── data
│   └── raw              # Dados brutos baixados da ANAC (CSV)
│       ├── arquivos_baixados.csv
├── notebooks
│   └── download.ipynb   # Notebook para download e pré-processamento
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
```

## ⚙️ Premissas
- O projeto considera como ponto de partida o ano 2000, quando a ANAC começou a disponibilizar os dados públicos.
- Os arquivos são baixados em formato CSV e armazenados na pasta data/raw.
- O objetivo inicial é criar uma base organizada para análises futuras.

## 🛠️ Como Usar

### 1. Clone o repositório

```
git clone https://github.com/jailtonmonteiro/download_anac_voos.git
```

### 2. Crie um ambiente virtual e instale as dependências

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Execute o notebook de download

Abra o arquivo notebooks/download.ipynb no Jupyter ou no VSCode e rode as células para baixar os arquivos CSV.

## 📊 Exemplo de Uso com Pandas

```
import pandas as pd

# Carregar um dos arquivos baixados
df = pd.read_csv("data/raw/VRA_20233.csv")

# Visualizar as primeiras linhas
print(df.head())
```

## 📦 Dependências

As dependências estão listadas no arquivo requirements.txt:

```
pandas>=2.0.0,<3.0.0
requests>=2.32.0,<3.0.0
jupyter
```

instale com:
```
pip install -r requirements.txt
```

## 📖 Referências

 - Portal ANAC – Dados Abertos (https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas)
 - Pandas Documentation (https://pandas.pydata.org/docs/#)
 - Requests Documentation (https://requests.readthedocs.io/en/latest/)
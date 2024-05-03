import  yfinance as yf  

lista_empresas = ["PETR4.SA", "ITAU",]

dados_empresa = yf.download(lista_empresas)

print(dados_empresa)


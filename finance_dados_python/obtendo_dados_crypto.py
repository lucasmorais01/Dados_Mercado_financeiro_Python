from cryptocmd import CmcScraper

scraper = CmcScraper("RSR")

dados_crypto = scraper.get_dataframe()

print(dados_crypto)
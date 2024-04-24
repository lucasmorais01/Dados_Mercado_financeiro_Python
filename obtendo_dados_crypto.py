from cryptocmd import CmcScraper

scraper = CmcScraper("ETH")

dados_crypto = scraper.get_dataframe()

print(dados_crypto)
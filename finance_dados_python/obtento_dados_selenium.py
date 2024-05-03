from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas   as pd   


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url_site = "https://www.fundamentus.com.br/resultado.php"

driver.get(url_site)


local_tabela = "/html/body/div[1]/div[2]/table"

elemento = driver.find_element("xpath", local_tabela)
html_tabela = elemento.get_attribute("outerHTML")
html_tabela

##print(html_tabela)

tabela = pd.read_html(str(html_tabela), thousands='.', decimal=',')[1]

print(tabela)
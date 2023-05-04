from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Precisei mudar a forma como acessamos o Firefox, o código fornecido nas aulas não funcionou aqui
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(executable_path=r'./geckodriver.exe', options=options)

browser.get('http://localhost:8000')

assert 'Django' in browser.title
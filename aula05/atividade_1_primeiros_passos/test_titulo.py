import pytest
from selenium import webdriver

def test_validar_titulo_do_site():
    # 1. Instanciamos o navegador Chrome
    navegador = webdriver.Chrome()
    
    try:
        # 2. Acesse a URL do Python
        navegador.get("https://www.python.org")

        # 3. Pegue o título da aba do navegador
        titulo_aba = navegador.title

        # 4. Crie o Assert para garantir que "Python" está escrito no título
        assert "Python" in titulo_aba
        
    finally:
        # Fecha o navegador para não travar o PC
        navegador.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buscar_na_wikipedia():
    navegador = webdriver.Chrome()
    # A janela padrão do Chrome abre pequena, e o layout responsivo da Wikipédia
    # esconde a barra de busca "desktop" nesse tamanho. Maximizar evita o erro
    # ElementNotInteractableException por elemento oculto no layout mobile.
    navegador.maximize_window()

    try:
        navegador.get("https://pt.wikipedia.org/")
        
        # 1. Ache a barra de pesquisa (O 'name' do input na Wiki é 'search')
        caixa_busca = navegador.find_element(By.NAME, "search")
        
        # 2. Digite "Teste de software" na caixa
        caixa_busca.send_keys("Teste de software")

        # 3. Aperte Enter (submeter o formulário)
        caixa_busca.submit()

        # A navegação disparada pelo submit não é instantânea: sem esperar,
        # o assert abaixo roda rápido demais e ainda pega o título da página antiga.
        WebDriverWait(navegador, 10).until(EC.title_contains("Teste de software"))

        # 4. Verifique se o título da nova aba contém "Teste de software"
        assert "Teste de software" in navegador.title
        
    finally:
        navegador.quit()
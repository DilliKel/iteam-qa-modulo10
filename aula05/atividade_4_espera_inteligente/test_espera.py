import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_esperar_elemento_lento_aparecer():
    navegador = webdriver.Chrome()
    
    try:
        # Este site de testes carrega e cria um elemento <p> após alguns segundos
        navegador.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        
        # 1. Clicar no botão 'Start' para iniciar o carregamento lento
        navegador.find_element(By.CSS_SELECTOR, "#start button").click()
        
        # 2. O texto "Hello World!" vai demorar uns 5 segundos para aparecer.
        # Se você tentar buscar agora, o teste quebra!
        
        # 3. Use o WebDriverWait para esperar ATÉ 10 segundos pelo elemento de ID 'finish'
        espera = WebDriverWait(navegador, 10)
        
        # Esperamos a condição "presença do elemento" ser verdadeira
        elemento_texto = espera.until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        
        # 4. Valide se deu certo!
        assert "Hello World!" in elemento_texto.text
        
    finally:
        navegador.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_com_sucesso():
    navegador = webdriver.Chrome()
    
    try:
        navegador.get("https://www.saucedemo.com/")
        
        # 1. Ache o campo de usuário (id = 'user-name') e digite: standard_user
        campo_usuario = navegador.find_element(By.ID, "user-name")
        campo_usuario.send_keys("standard_user")

        # 2. Ache o campo de senha (id = 'password') e digite: secret_sauce
        campo_senha = navegador.find_element(By.ID, "password")
        campo_senha.send_keys("secret_sauce")

        # 3. Ache o botão de login (id = 'login-button') e clique nele
        botao_login = navegador.find_element(By.ID, "login-button")
        botao_login.click()
        
        # 4. Validar se entrou no sistema
        assert "inventory.html" in navegador.current_url
        
    finally:
        navegador.quit()
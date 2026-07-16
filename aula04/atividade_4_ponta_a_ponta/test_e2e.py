from fluxo import BancoReal, ControladorHTTP, InterfaceUsuario

def test_fluxo_completo_ponta_a_ponta():
    # 1. PREPARAÇÃO (Encaixe as peças de baixo para cima / Bottom-up!)
    banco = BancoReal()
    controlador = ControladorHTTP(banco)
    interface = InterfaceUsuario(controlador)

    # 2. AÇÃO (O usuário clica no botão salvar)
    resultado = interface.clicar_botao_salvar("Mouse Gamer")

    # 3. VALIDAÇÃO E2E (Valide se o 'resultado' é OK e se o 'Mouse Gamer' está dentro do banco.tabela!)
    assert resultado == "OK"
    assert "Mouse Gamer" in banco.tabela
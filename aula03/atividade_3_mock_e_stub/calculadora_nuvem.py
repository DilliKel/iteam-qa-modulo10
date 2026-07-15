from api_cliente import consultar_tipo_cliente_na_api

def calcular_desconto_por_cpf(valor_total, cpf):
    # Dependência Externa! Vai na internet buscar a informação:
    tipo_cliente = consultar_tipo_cliente_na_api(cpf)
    
    if tipo_cliente == "VIP":
        return valor_total * 0.20
    return 0.0
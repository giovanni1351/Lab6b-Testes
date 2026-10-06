def isento(pcd, valor_compra, cadastro_app, minutos):
    # Defeito proposital: o cadastro ignora o limite de permanência.
    return bool(pcd or (valor_compra >= 150.00 and minutos <= 240) or cadastro_app)

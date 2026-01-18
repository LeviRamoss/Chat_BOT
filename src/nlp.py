def normalizar_texto(texto):
    return texto.lower().strip()

def identificar_conceito(texto, conceitos_disponiveis):
    for conceito in conceitos_disponiveis:
        if conceito in texto:
            return conceito
    return None

import random

def responder_conceito(conceito, base_conhecimento):
    dados = base_conhecimento[conceito]

    resposta = (
        f"{dados['titulo']}\n"
        f"{dados['definicao']}\n\n"
        f"{dados['detalhamento']}\n"
        f"Exemplos:\n"
    )

    for exemplo in dados["exemplos"]:
        resposta += f"- {exemplo}\n"

    return resposta


def responder_dialogo(tipo, base_dialogo):
    return random.choice(base_dialogo[tipo])

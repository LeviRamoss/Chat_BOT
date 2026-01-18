import os
import json

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")

BASE_CONHECIMENTO_PATH = os.path.join(DATA_DIR, "base_conhecimento.json")
BASE_DIALOGO_PATH = os.path.join(DATA_DIR, "base_conhecimento_dialogo.json")

base_conhecimento = carregar_json(BASE_CONHECIMENTO_PATH)
base_dialogo = carregar_json(BASE_DIALOGO_PATH)


from nlp import normalizar_texto, identificar_conceito
from resposta import responder_conceito, responder_dialogo

print(responder_dialogo("saudacoes", base_dialogo))

while True:
    pergunta = input("\nUsuário: ")

    if pergunta.lower() in ["sair", "exit", "encerrar"]:
        print(responder_dialogo("despedidas", base_dialogo))
        break

    texto = normalizar_texto(pergunta)
    conceito = identificar_conceito(texto, base_conhecimento.keys())

    if conceito:
        print("\nBot:")
        print(responder_conceito(conceito, base_conhecimento))
        print(responder_dialogo("confirmacao", base_dialogo))
    else:
        print("\nBot:")
        print(responder_dialogo("nao_entendido", base_dialogo))

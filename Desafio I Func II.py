def processador_texto(texto, **kwargs):
    # Função para contar palavras
    contar_palavras = lambda txt: len(txt.split())
    
    # Função para contar letras
    contar_letras = lambda txt: len(txt.replace(' ', ''))
    
    # Função para inverter o texto
    inverter_texto = lambda txt: txt[::-1]
    
    # Função para substituir uma palavra por outra
    substituir_palavra = lambda txt, antiga, nova: txt.replace(antiga, nova)
    
    # Aplicar as operações especificadas em kwargs
    for operacao, valor in kwargs.items():
        if operacao == "contar_palavras":
            print(f"Número de palavras: {contar_palavras(texto)}")
        elif operacao == "contar_letras":
            print(f"Número de letras: {contar_letras(texto)}")
        elif operacao == "inverter_texto":
            texto = inverter_texto(texto)
        elif operacao == "substituir_palavra":
            if "nova_palavra" in kwargs:
                texto = substituir_palavra(texto, valor, kwargs["nova_palavra"])
            else:
                print("Erro: 'nova_palavra' não foi fornecida para substituição.")
    
    return texto

# Exemplo de uso
texto = "Olá mundo! Este é um exemplo de processamento de texto."
resultado = processador_texto(
    texto,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=True,
    substituir_palavra="exemplo",
    nova_palavra="teste"
)

print("Texto final:", resultado)
faq = {
    ("horario", "horários", "funcionamento", "aberto"): "Estamos abertos das 8h às 18h.",
    ("curso", "cursos", "programacao", "ia"): "Oferecemos cursos de programação e IA.",
    ("contato", "telefone", "whatsapp", "ligar"): "Nosso telefone é (14) 1234-5678."
}

termo_busca = "qual é o horario de funcionado"

# Percorre cada chave (tupla) do dicionário
for chave in faq:
    # Percorre cada palavra individual dentro da tupla atual
    for palavra in chave:
        # Verifica se a palavra-chave está contida na frase de busca
        if palavra in termo_busca:
            print(faq[chave])
            break # Sai do laço interno para não repetir a mesma resposta
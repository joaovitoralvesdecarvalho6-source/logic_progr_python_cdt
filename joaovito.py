def lavar_cabelo(tipo_cabelo):
    print('--- Lavando o cabelo: Sistema Simples ---')
    print('Manual de como lavar o cabelo:')
    print('1. Pegar um shampoo, esfregar o cabelo e enxaguar')
    print('2. Lavar o cabelo com shampoo novamente')
    print('3. Passar máscara de cabelo com óleo capilar, esperar 20 minutos e enxaguar')
    print('4. Último passo: passar condicionador')
    print('5. Secar o cabelo com toalha ou secador')
    print('6. Depois, passar um creme com óleo capilar')
    print('--- Fim do sistema simples ---\n')

    # Trata o texto removendo espaços extras nas pontas e padronizando para minúsculas
    estado = tipo_cabelo.strip().lower()

    if estado == 'lavando':
        resultado = 'Cabelo molhado com shampoo cheiroso!'
    elif estado == 'cabelo molhado':
        resultado = 'Desembaraçando o cabelo!'
    else:
        resultado = 'Cabelo com creme finalizado!'
        
    return resultado

# --- Exemplos de Uso ---

# Teste 1: Estado "lavando"
print("Teste 1:")
resultado_1 = lavar_cabelo('lavando')
print(f"Resultado: {resultado_1}\n")

# Teste 2: Estado "cabelo molhado"
print("Teste 2:")
resultado_2 = lavar_cabelo('cabelo molhado')
print(f"Resultado: {resultado_2}\n")

# Teste 3: Outro estado (ex: "seco" ou "finalizado")
print("Teste 3:")
resultado_3 = lavar_cabelo('finalizado')
print(f"Resultado: {resultado_3}\n")





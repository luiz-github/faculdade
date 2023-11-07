# Variáveis iniciais
total_abono = 0
total_funcionarios = 0
funcionarios_minimo = 0
maior_abono = 0

# Solicita a entrada de salários dos funcionários
while True:
    salario = float(input("Digite o salário do funcionário (0 para encerrar): "))
    
    # Verifica se a entrada é zero para encerrar
    if salario == 0:
        break
    
    # Calcula o abono com base nas regras
    abono = max(salario * 0.20, 100)
    
    # Atualiza os valores
    total_abono += abono
    total_funcionarios += 1
    if abono == 100:
        funcionarios_minimo += 1
    if abono > maior_abono:
        maior_abono = abono
    
    # Exibe os resultados para o funcionário atual
    print(f"Salário: R$ {salario:.2f} | Abono: R$ {abono:.2f}\n")

# Exibe os resultados gerais
print(f"Total de funcionários processados: {total_funcionarios}")
print(f"Total a ser gasto com o pagamento do abono: R$ {total_abono:.2f}")
print(f"Funcionários que receberão o valor mínimo de R$ 100: {funcionarios_minimo}")
print(f"Maior valor pago como abono: R$ {maior_abono:.2f}")

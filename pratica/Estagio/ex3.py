import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

faturamentoFiltrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menorValor = min(faturamentoFiltrado)
maiorValor = max(faturamentoFiltrado)

mediaMensal = sum(faturamentoFiltrado) / len(faturamentoFiltrado)

diasAcimaDaMedia = len([valor for valor in faturamentoFiltrado if valor > mediaMensal])

print(f"Menor valor de faturamento: R$ {menorValor:.2f}")
print(f"Maior valor de faturamento: R$ {maiorValor:.2f}")
print(f"Número de dias com faturamento acima da média: {diasAcimaDaMedia}")

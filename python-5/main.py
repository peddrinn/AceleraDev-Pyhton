from datetime import datetime

records = [
    {
        'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674
        },
    {
        'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821
        },
    {
        'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838
        },
    {
        'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258
        },
    {
        'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317
        },
    {
        'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821
        },
    {
        'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {
        'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821
        },
    {
        'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821
        },
    {
        'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150
        },
    {
        'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821
        },
    {
        'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000
        }
]

def calcula_custo_chamada(inicio_chamada, fim_chamada):

    hora_inicio = int(datetime.fromtimestamp(inicio_chamada).hour)
    hora_fim = int(datetime.fromtimestamp(fim_chamada).hour)

    tempo_ligacao = (fim_chamada - inicio_chamada) // 60

    if 6 <= hora_inicio < 22:
        custo_ligacao = 0.36 + tempo_ligacao * 0.09        
    else:
        custo_ligacao = 0.36
    
    return round(custo_ligacao, 2)

def classify_by_phone_number(records):

    telefones = []

    for chamada in records:

        # flag para verificar se o telefone é novo ou não
        tel = 0
        # Calcula o custo de cada chamada
        custo_chamada = calcula_custo_chamada(chamada['start'],chamada['end'])
        
        for telefone in telefones:
            # verifica se o numero de origem já esta incluido
            # na lista de telefones
            if chamada['source'] in telefone.values():
                tel = 1
                # soma o custo da chamada atual com os custos
                # anteriores  do telefone
                total = round((telefone['total'] + custo_chamada), 2)
                telefone['total'] = total

        if tel == 0:
            # insere um novo numero na lista de telefones
            telefones.append({'source': chamada['source'], 'total': custo_chamada})

    # Ordena os telefones em ordem decrescente
    telefones_ordenados = sorted(telefones, key=lambda tels: tels['total'], reverse=True)

    return telefones_ordenados
 


classify_by_phone_number(records)
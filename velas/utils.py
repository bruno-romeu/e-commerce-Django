import requests 
from decouple import config

def calcular_frete_melhor_envio(cep_origem, cep_destino, peso, altura, diâmetro, circunferência):
    url = "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate"
    headers = {
        'Authorization': config("API_KEY"),

        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    data = {
        'from': {'postal_code': cep_origem},
        'to': {'postal_code': cep_destino},
        'products':[
            {
                'weight': peso,
                'width': diâmetro,
                'height': circunferência,
                'length': altura,
                'quantity': 1
            }
        ],
        'services': ['SEDEX'],
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code==200:
        return response.json()
    else:
        raise Exception(f'Erro na API Melhor Envio: {response.status_code} {response.text}')
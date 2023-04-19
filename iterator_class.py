import requests


class BitcoinIterator:
    """
    Doc string:

    Classe que itera sobre os preços atuais de uma moeda obtidos de uma API.

    Atributos:
        preços (dict): Dicionário com informações sobre os preços atuais da moeda em diferentes cotações
        current (int): Índice atual do dicionário de preços.
        end (int): Tamanho do dicionário de preços.

    Métodos:
        __iter__: Implementação padrão do método mágico __iter__
        __next__: Implementação padrão do método mágico __next__
    """
    def __init__(self, coin_name: str):
        """
        Construtor da class.

        Argumentos:
            :param coin_name (str): Nome da moeda a ser buscada na API
        """
        self.coin_name = coin_name
        self.url = f"https://api.coingecko.com/api/v3/coins/{coin_name}"
        response = requests.get(self.url)
        data = response.json()
        self.prices = data["market_data"]["current_price"]

        # Instanciando estado atual e final da iteração

        self.current = 0
        self.end = len(self.prices)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = list(self.prices.items())[self.current]
        self.current += 1
        return result

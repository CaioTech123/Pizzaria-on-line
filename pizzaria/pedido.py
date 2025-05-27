class Pedido:
    def __init__(self, cliente, pizza):
        self.cliente = cliente
        self.pizza = pizza

    def __str__(self):
        return f"Pedido de {self.cliente.nome} - {self.pizza.tamanho} {self.pizza.sabor} - R${self.pizza.preco:.2f}"

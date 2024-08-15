
class ListaProdutos:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def mostrar_produtos(self):
        for p in self.produtos:
            print(p)
            
    def buble_sort(self):
        for i in range(len(self.produtos)):
            for j in range(len(self.produtos) - 1):
                if self.produtos[j].preco > self.produtos[j + 1].preco:
                    aux = self.produtos[j]
                    self.produtos[j] = self.produtos[j + 1]
                    self.produtos[j + 1] = aux
                    #  self.produtos[j], self.produtos[j + 1] = self.produtos[j + 1], self.produtos[j]
                    
    def buscar_produto(self, nome):
        if nome is None:
            raise ValueError("Nome can't be null")
        start = 0
        end = len(self.produtos) - 1
        if start > end:
            return None
        while start <= end:
            middle = start + (end - start) // 2
            test = self.produtos[middle].nome
            if test == nome:
                return f'Position: {middle} | {self.produtos[middle]}'
            if test > nome:
                end = middle - 1
            else:
                start = middle +1
        return None

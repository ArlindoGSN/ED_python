class ListaProdutos:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def mostrar_produtos(self):
        for p in self.produtos:
            print(p)

    def bubble_sort(self):
        n = len(self.produtos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.produtos[j].preco > self.produtos[j + 1].preco:
                    self.produtos[j], self.produtos[j + 1] = self.produtos[j + 1], self.produtos[j]
    def buscar_produto_nome(self, nome):
        start = 0
        end = len(self.produtos) - 1
        while start <= end:
            middle = start + (end - start ) // 2
            if self.produtos[middle].nome == nome:
                return self.produtos[middle]
            elif self.produtos[middle].nome > nome:
                end = middle - 1
            else:
                start = middle + 1
        return None

    def buscar_produto_preco(self, preco_baixo, preco_max):
        self.bubble_sort()  
        start = 0
        end = len(self.produtos) - 1
        lista = []

        while start <= end:
            middle = start + (end - start) // 2
            test = self.produtos[middle].preco
            if preco_baixo <= test <= preco_max:
                lista.append(self.produtos[middle])
                left = middle - 1
                while left >= 0 and preco_baixo <= self.produtos[left].preco <= preco_max:
                    lista.append(self.produtos[left])
                    left -= 1
                right = middle + 1
                while right < len(self.produtos) and preco_baixo <= self.produtos[right].preco <= preco_max:
                    lista.append(self.produtos[right])
                    right += 1
                break  
            elif test > preco_max:
                end = middle - 1
            else:
                start = middle + 1
        
        return lista

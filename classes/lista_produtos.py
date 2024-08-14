
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
                    self.produtos[j], self.produtos[j + 1] = self.produtos[j + 1], self.produtos[j]
                    
    def buscar_produto(self, nome):
        start = 0
        end = len(self.produtos) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.produtos[mid].nome == nome:
                return self.produtos[mid]
            elif self.produtos[mid].nome < nome:
                start = mid + 1
            else:
                end = mid - 1
        return None
            
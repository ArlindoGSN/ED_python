from classes import produto, lista_produtos

def main():
 
    lista = lista_produtos.ListaProdutos()
    lista.adicionar_produto(produto.Produto("Coca Cola", 5.00))
    lista.adicionar_produto(produto.Produto("Sorvete", 6.00))
    lista.adicionar_produto(produto.Produto("Cerveja", 4.00))
    lista.adicionar_produto(produto.Produto("Suco", 8.00))
    lista.adicionar_produto(produto.Produto("Agua", 3.00))

    lista.mostrar_produtos()
    lista.buble_sort()
    print("Ordenado:")
    lista.mostrar_produtos()
    print("Busca:")
    print(lista.buscar_produto("Suco"))
        
main()
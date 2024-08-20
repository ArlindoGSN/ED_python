from classes import produto, lista_produtos

def main():
    lista = lista_produtos.ListaProdutos()
    lista.adicionar_produto(produto.Produto("Coca Cola", 5.00))
    lista.adicionar_produto(produto.Produto("Sorvete", 6.00))
    lista.adicionar_produto(produto.Produto("Cerveja", 4.00))
    lista.adicionar_produto(produto.Produto("Suco", 8.00))
    lista.adicionar_produto(produto.Produto("Agua", 3.00))

    lista.mostrar_produtos()
    lista.bubble_sort()
    print("Ordenado:")
    lista.mostrar_produtos()
    print("Busca por preço:")
    produtos_encontrados = lista.buscar_produto_preco(5.00, 8.00)
    print([str(produto) for produto in produtos_encontrados])

if __name__ == "__main__":    
    main()
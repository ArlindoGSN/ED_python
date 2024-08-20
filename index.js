// Definição da classe Produto
class Produto {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }
}

// Exemplo de criação de um array de produtos
let produtos = [
    new Produto("Produto A", 30.00),
    new Produto("Produto B", 20.00),
    new Produto("Produto C", 10.00),
    new Produto("Produto D", 50.00),
    new Produto("Produto E", 40.00)
];

// Função para ordenar os produtos pelo preço usando Bubble Sort
function bubbleSort(produtos) {
    let n = produtos.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - 1 - i; j++) {
            if (produtos[j].preco > produtos[j + 1].preco) {
                // Troca os elementos
                let temp = produtos[j];
                produtos[j] = produtos[j + 1];
                produtos[j + 1] = temp;
            }
        }
    }
}

// Função para realizar a busca binária do primeiro índice de produto que está na faixa de preço
function buscaBinariaPorPrecoMin(produtos, precoMin) {
    let low = 0;
    let high = produtos.length - 1;
    let index = produtos.length; // Inicialmente define um índice fora do intervalo

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (produtos[mid].preco < precoMin) {
            low = mid + 1;
        } else {
            index = mid;
            high = mid - 1;
        }
    }

    return index;
}

// Função para realizar a busca binária do último índice de produto que está na faixa de preço
function buscaBinariaPorPrecoMax(produtos, precoMax) {
    let low = 0;
    let high = produtos.length - 1;
    let index = -1; // Inicialmente define um índice fora do intervalo

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (produtos[mid].preco <= precoMax) {
            index = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return index;
}

// Função para buscar produtos por faixa de preço usando busca binária
function buscaPorFaixaDePreco(produtos, precoMin, precoMax) {
    let resultado = [];

    // Ordena os produtos pelo preço
    bubbleSort(produtos);
    console.log("Produtos ordenados por preço:", produtos);

    // Encontra o índice do primeiro e último produto na faixa de preço
    let indexMin = buscaBinariaPorPrecoMin(produtos, precoMin);
    let indexMax = buscaBinariaPorPrecoMax(produtos, precoMax);

    // Adiciona produtos na faixa de preço ao resultado
    for (let i = indexMin; i <= indexMax; i++) {
        if (i >= 0 && i < produtos.length) {
            resultado.push(produtos[i]);
        }
    }

    return resultado;
}

// Busca produtos dentro de uma faixa de preço
console.log('Preço minimo: 20, Preço máximo: 40');
let produtosFaixaPreco = buscaPorFaixaDePreco(produtos, 20, 40);
if (produtosFaixaPreco.length > 0) {
    console.log("Produtos encontrados na faixa de preço:", produtosFaixaPreco);
} else {
    console.log("Nenhum produto encontrado na faixa de preço.");
}
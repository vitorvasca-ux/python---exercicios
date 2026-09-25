import matplotlib.pyplot as plt


class Produto:
    def __init__(self, nome, preco, categoria, estoque):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque
    
    # Produto impresso definido pelo método __str__

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Categoria: {self.categoria}, Estoque: {self.estoque}"

catalogo = []
categorias = []


def adicionar_produto(nome, preco, categoria, estoque):
    novo_produto = Produto(nome, preco, categoria, estoque)
    catalogo.append(novo_produto)
    categorias.append(categoria)
    print(f"Produto '{nome}' adicionado ao catálogo.")


def listar_catalogo():
    if not catalogo:
        print("O catálogo está vazio.")
    else:
        print("\n--- CATALOGO DE PRODUTOS ---")
        for produto in catalogo:
            print(produto)


if __name__ == "__main__":
    adicionar_produto("notebook", 2500.00, "eletrônicos", 10)
    adicionar_produto("smartphone", 1500.00, "eletrônicos", 20)
    adicionar_produto("geladeira", 3000.00, "eletrodomésticos", 5)
    adicionar_produto("fogão", 1200.00, "eletrodomésticos", 8)
    adicionar_produto("sofá", 2000.00, "móveis", 3)

    listar_catalogo()

    categorias_unicas = list(set(categorias))
    categorias_unicas.sort()
    contagem = [categorias.count(cat) for cat in categorias_unicas]

    plt.bar(categorias_unicas, contagem)
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade de Produtos")
    plt.title("Minha Loja - Produtos por Categoria")
    plt.show()
from src.biblioteca import Biblioteca
from src.livro import Livro


def main():
    biblioteca = Biblioteca()
    novo_livro = biblioteca.cadastrar_livro(
        "O Senhor dos Anéis", "J.R.R. Tolkien", "1954"
    )
    l_2 = biblioteca.cadastrar_livro("O Senhor dos Anéis 2", "J.R.R. Tolkien", "1956")
    novo_usuario = biblioteca.cadastrar_usuario("Alice", 30)
    biblioteca.emprestar_livro(novo_livro, novo_usuario)
    info = novo_livro.informacoes_livro()
    print(info)
    info = l_2.informacoes_livro()
    print(info)


if __name__ == "__main__":
    main()

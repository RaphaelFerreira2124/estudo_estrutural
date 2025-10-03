class Usuario:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.livros_emprestados = []

    def emprestar_livro(self, livro) -> None:
        """Adiciona um livro à lista de livros emprestados"""
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro) -> None:
        """Remove um livro da lista de livros emprestados"""
        self.livros_emprestados.remove(livro)

    def listar_livros_emprestados(self) -> list:
        """Retorna a lista de livros emprestados"""
        return self.livros_emprestados

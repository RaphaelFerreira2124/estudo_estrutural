import typing


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def informacoes_livro(self) -> str:
        """Retorna as informações do livro"""
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}"

    def emprestar(self) -> None:
        """Marca o livro como emprestado"""
        if self.disponivel:
            self.disponivel = False
        else:
            raise Exception("Livro indisponível para empréstimo.")

    def devolver(self) -> None:
        """Marca o livro como disponível"""
        self.disponivel = True

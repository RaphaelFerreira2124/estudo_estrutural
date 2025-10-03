from src.livro import Livro
from src.usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, titulo: str, autor: str, ano: int) -> Livro:
        """Cria e cadastra um livro na biblioteca"""
        livro = Livro(titulo, autor, ano)
        self.livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
        return livro

    def cadastrar_usuario(self, nome, idade) -> None:
        """Adiciona um usuário à biblioteca"""
        usuario = Usuario(nome, idade)
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso!")
        return usuario

    def emprestar_livro(self, livro: str, usuario: str) -> None:
        """Empresta um livro a um usuário"""
        print(livro.titulo)
        if livro not in self.livros:
            raise Exception(f"Livro '{livro.titulo}' não cadastrado na biblioteca.")
        if usuario not in self.usuarios:
            raise Exception(f"Usuário '{usuario.nome}' não cadastrado na biblioteca.")

        livro.emprestar()
        usuario.emprestar_livro(livro)
        print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}")

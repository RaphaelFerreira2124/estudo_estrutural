import pytest
from src.biblioteca import Biblioteca
from src.livro import Livro
from src.usuario import Usuario

class TestBiblioteca:
    def test_cadastrar_livro(self):
        biblioteca = Biblioteca()
        livro = biblioteca.cadastrar_livro("O Alquimista", "Paulo Coelho", 1988)
        
        assert livro in biblioteca.livros
        assert livro.titulo == "O Alquimista"
        assert livro.autor == "Paulo Coelho"
        assert livro.ano == 1988
        assert livro.disponivel

    def test_cadastrar_usuario(self):
        biblioteca = Biblioteca()
        usuario = biblioteca.cadastrar_usuario("Maria", 28)
        
        assert usuario in biblioteca.usuarios
        assert usuario.nome == "Maria"
        assert usuario.idade == 28
        assert usuario.livros_emprestados == []

    def test_emprestar_livro_sucesso(self):
        biblioteca = Biblioteca()
        livro = biblioteca.cadastrar_livro("O Alquimista", "Paulo Coelho", 1988)
        usuario = biblioteca.cadastrar_usuario("Maria", 28)
        
        biblioteca.emprestar_livro(livro, usuario)
        
        assert not livro.disponivel
        assert livro in usuario.livros_emprestados

    def test_emprestar_livro_indisponivel(self):
        biblioteca = Biblioteca()
        livro = biblioteca.cadastrar_livro("O Alquimista", "Paulo Coelho", 1988)
        usuario1 = biblioteca.cadastrar_usuario("Maria", 28)
        usuario2 = biblioteca.cadastrar_usuario("João", 35)
        
        biblioteca.emprestar_livro(livro, usuario1)
        
        with pytest.raises(Exception) as excinfo:
            biblioteca.emprestar_livro(livro, usuario2)
        
        assert str(excinfo.value) == "Livro indisponível para empréstimo."

    def test_emprestar_livro_nao_cadastrado(self):
        biblioteca = Biblioteca()
        livro = Livro("Livro Não Cadastrado", "Autor Desconhecido", 2020)
        usuario = biblioteca.cadastrar_usuario("Maria", 28)
        
        with pytest.raises(Exception) as excinfo:
            biblioteca.emprestar_livro(livro, usuario)
        
        assert str(excinfo.value) == f"Livro '{livro.titulo}' não cadastrado na biblioteca."


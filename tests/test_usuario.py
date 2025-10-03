import pytest
from src.usuario import Usuario

class TestUsuario:
    def test_emprestar_livro(self):
        usuario = Usuario("João", 25)
        livro_mock = "Livro Mock"
        
        usuario.emprestar_livro(livro_mock)
        
        assert livro_mock in usuario.livros_emprestados

    def test_devolver_livro(self):
        usuario = Usuario("João", 25)
        livro_mock = "Livro Mock"
        
        usuario.emprestar_livro(livro_mock)
        usuario.devolver_livro(livro_mock)
        
        assert livro_mock not in usuario.livros_emprestados

    def test_listar_livros_emprestados(self):
        usuario = Usuario("João", 25)
        livro_mock1 = "Livro Mock 1"
        livro_mock2 = "Livro Mock 2"
        
        usuario.emprestar_livro(livro_mock1)
        usuario.emprestar_livro(livro_mock2)
        
        livros = usuario.listar_livros_emprestados()
        
        assert livro_mock1 in livros
        assert livro_mock2 in livros
        assert len(livros) == 2
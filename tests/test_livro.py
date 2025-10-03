import pytest
from src.livro import Livro

class TestLivro:
    def test_informacoes_livro(self):
        livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
        
        info = livro.informacoes_livro()
        
        assert "Dom Casmurro" in info
        assert "Machado de Assis" in info
        assert "1899" in info
        assert "Disponível" in info

    def test_emprestar_livro_disponivel(self):
        livro = Livro("1984", "George Orwell", 1949)
        livro.emprestar()
        assert not livro.disponivel

    def test_emprestar_livro_indisponivel(self):
        livro = Livro("1984", "George Orwell", 1949)
        livro.emprestar()
        with pytest.raises(Exception) as excinfo:
            livro.emprestar()
        assert str(excinfo.value) == "Livro indisponível para empréstimo."

    def test_devolver_livro(self):
        livro = Livro("1984", "George Orwell", 1949)
        livro.emprestar()
        livro.devolver()
        assert livro.disponivel
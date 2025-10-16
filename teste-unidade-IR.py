import unittest
# Importa a função a ser testada do arquivo onde ela está implementada
from calculo_ir import calcular_ir 

class TestCalculoIR(unittest.TestCase):
  
    # ====================================================================
    # Testes de Exceção/Caminho de Erro (GFC Caminho 1 / PCE I1)
    # ====================================================================

    def test_caminho_erro_negativo(self):
        """Testa Base de Cálculo negativa (Caminho 1 do GFC)."""
        resultado = calcular_ir(-100.00)
        self.assertIn("Erro: Valor Inválido", resultado)

    def test_caminho_erro_nao_numerico(self):
        """Testa entrada não numérica (PCE I2)."""
        resultado = calcular_ir("dez mil")
        self.assertIn("Erro: Valor Inválido", resultado)

    # ====================================================================
    # Testes Válidos - Limites Superiores das Faixas (GFC Caminhos 2-5)
    # ====================================================================
    
    def test_caminho_faixa_0_limite_superior(self):
        """Testa limite superior da isenção (R$ 2.259,20 - GFC Caminho 2)."""
        resultado = calcular_ir(2259.20)
        self.assertEqual(resultado, "IR: R$0.00 (Alíquota Aplicada: 0.0%)")

    def test_caminho_faixa_7_5_limite_superior(self):
        """Testa limite superior da faixa de 7,5% (R$ 2.826,65 - GFC Caminho 3)."""
        # Cálculo esperado: (2826.65 * 0.075) - 169.44 = 42.55875 => R$ 42,56
        resultado = calcular_ir(2826.65)
        self.assertEqual(resultado, "IR: R$42.56 (Alíquota Aplicada: 7.5%)")

    def test_caminho_faixa_15_limite_superior(self):
        """Testa limite superior da faixa de 15% (R$ 3.751,05 - GFC Caminho 4)."""
        # Cálculo esperado: (3751.05 * 0.15) - 381.44 = 181.2175 => R$ 181,22
        resultado = calcular_ir(3751.05)
        self.assertEqual(resultado, "IR: R$181.22 (Alíquota Aplicada: 15.0%)")

    def test_caminho_faixa_22_5_limite_superior(self):
        """Testa limite superior da faixa de 22,5% (R$ 4.664,68 - GFC Caminho 5)."""
        # Cálculo esperado: (4664.68 * 0.225) - 662.77 = 386.303 => R$ 386,30
        resultado = calcular_ir(4664.68)
        self.assertEqual(resultado, "IR: R$386.30 (Alíquota Aplicada: 22.5%)")

    # ====================================================================
    # Testes Válidos - Início de Faixas (AVL Limites Inferiores)
    # ====================================================================

    def test_avl_faixa_7_5_limite_inferior(self):
        """Testa o valor mínimo para entrar na faixa de 7,5% (R$ 2.259,21)."""
        # Cálculo esperado: (2259.21 * 0.075) - 169.44 = 0.00075 => R$ 0,00
        resultado = calcular_ir(2259.21)
        self.assertEqual(resultado, "IR: R$0.00 (Alíquota Aplicada: 7.5%)")

    def test_caminho_faixa_27_5_limite_inferior(self):
        """Testa o valor mínimo para entrar na faixa de 27,5% (R$ 4.664,69 - GFC Caminho 6)."""
        # Cálculo esperado: (4664.69 * 0.275) - 896.00 = 392.99 => R$ 392,99
        resultado = calcular_ir(4664.69)
        self.assertEqual(resultado, "IR: R$392.99 (Alíquota Aplicada: 27.5%)")
        
    def test_faixa_27_5_valor_medio(self):
        """Testa um valor médio dentro da faixa de 27,5% (R$ 10.000,00)."""
        # Cálculo esperado: (10000 * 0.275) - 896.00 = 1854.00 => R$ 1.854,00
        resultado = calcular_ir(10000.00)
        self.assertEqual(resultado, "IR: R$1854.00 (Alíquota Aplicada: 27.5%)")

if __name__ == '__main__':
    # Para rodar o teste via linha de comando: python -m unittest test_ir.py
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
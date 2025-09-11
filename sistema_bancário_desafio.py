import unittest
from banco import Cliente, ContaBancaria


class TestBanco(unittest.TestCase):

    def setUp(self):
        """Método executado antes de cada teste. Inicializa o estado."""
        self.cliente1 = Cliente("Maria Oliveira", "987.654.321-00")
        self.cliente2 = Cliente("José Souza", "123.456.789-10")
        self.cliente3 = Cliente("Ana Costa", "111.222.333-44")
        self.cliente1.criar_conta()
        self.cliente2.criar_conta()
        self.cliente3.criar_conta()

    def test_criar_conta(self):
        """Testa a criação de uma conta para um cliente."""
        self.assertIsNotNone(self.cliente1.conta, "A conta não foi criada para o cliente.")
        self.assertIsNotNone(self.cliente2.conta, "A conta não foi criada para o cliente.")
        self.assertIsNotNone(self.cliente3.conta, "A conta não foi criada para o cliente.")

    def test_depositar(self):
        """Testa a funcionalidade de depósito na conta."""
        self.cliente1.conta.depositar(1000)
        self.assertEqual(self.cliente1.conta.saldo, 1000, "O depósito não foi realizado corretamente.")

        # Testando um valor inválido (negativo)
        saldo_anterior = self.cliente1.conta.saldo
        self.cliente1.conta.depositar(-500)
        self.assertEqual(self.cliente1.conta.saldo, saldo_anterior, "Depósitos negativos não devem ser permitidos.")

    def test_sacar(self):
        """Testa a funcionalidade de saque da conta."""
        self.cliente2.conta.depositar(1000)
        self.cliente2.conta.sacar(500)
        self.assertEqual(self.cliente2.conta.saldo, 500, "O saque não foi realizado corretamente.")

        # Testando o saque com valor maior que o saldo
        saldo_anterior = self.cliente2.conta.saldo
        self.cliente2.conta.sacar(1001)
        self.assertEqual(self.cliente2.conta.saldo, saldo_anterior, "O saque não pode ser superior ao saldo.")

        # Testando o saque com valor negativo
        saldo_anterior = self.cliente2.conta.saldo
        self.cliente2.conta.sacar(-100)
        self.assertEqual(self.cliente2.conta.saldo, saldo_anterior, "O saque de valores negativos não deve ser permitido.")

    def test_limite_saques(self):
        """Testa o limite de saques na conta do cliente."""
        self.cliente3.conta.depositar(2000)

        # Realizando o primeiro saque
        self.cliente3.conta.sacar(500)
        self.assertEqual(self.cliente3.conta.saldo, 1500, "O primeiro saque não foi realizado corretamente.")

        # Realizando o segundo saque
        self.cliente3.conta.sacar(500)
        self.assertEqual(self.cliente3.conta.saldo, 1000, "O segundo saque não foi realizado corretamente.")

        # Tentando fazer um saque a mais do que o limite
        self.cliente3.conta.sacar(500)
        self.assertEqual(self.cliente3.conta.saldo, 500, "O limite de saques não foi respeitado.")
        
        # Tentando realizar um quarto saque (deve falhar)
        saldo_anterior = self.cliente3.conta.saldo
        self.cliente3.conta.sacar(500)
        self.assertEqual(self.cliente3.conta.saldo, saldo_anterior, "Deve ser possível realizar no máximo 3 saques.")

    def test_extrato(self):
        """Testa a geração do extrato da conta."""
        self.cliente1.conta.depositar(1000)
        self.cliente1.conta.sacar(500)
        extrato = self.cliente1.conta.extrato
        self.assertIn("Depósito:", extrato, "O extrato não contém informações sobre o depósito.")
        self.assertIn("Saque:", extrato, "O extrato não contém informações sobre o saque.")
        self.assertIn("Saldo:", extrato, "O extrato não contém informações sobre o saldo final.")

    def tearDown(self):
        """Método executado após cada teste. Limpa qualquer dado global/modificado."""
        # Este método pode ser usado para limpar recursos externos ou reiniciar objetos, mas aqui não há necessidade
        pass


if __name__ == '__main__':
    unittest.main()

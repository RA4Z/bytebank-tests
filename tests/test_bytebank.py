from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When-ação
        resultado = funcionario_teste.idade()

        #Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Robert_Zimmermann_deve_retornar_Zimmermann():
        entrada = 'Robert Zimmermann'
        esperado = 'Zimmermann'

        robert = Funcionario(entrada, '31/07/2003', 1111)

        resultado = robert.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Robert Zimmermann'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '31/07/2003', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

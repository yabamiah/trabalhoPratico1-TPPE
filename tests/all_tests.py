import unittest

from tests import test_classificacao
from tests import test_gerador_rodadas
from tests import test_partida
from tests import test_processamento_resultados
from tests import test_time
from tests import test_integracao_campeonato

def suite():
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_classificacao))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_gerador_rodadas))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_partida))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_processamento_resultados))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_time))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_integracao_campeonato))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
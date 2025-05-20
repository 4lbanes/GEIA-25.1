from importar import ImportarDados
from analise import AnaliseEstatistica

class Main():
    caminho = 'base.csv' 
    importador = ImportarDados(caminho)
    dados, ids = importador.importar()

    colunas = ['Idade', 'Nota_Matematica', 'Nota_Estatistica', 'Nota_Programacao', 'Faltas']
    AnaliseEstatistica.generate_report(dados, ids, colunas)

if __name__ == "__Main__":
    Main()
    
        
    
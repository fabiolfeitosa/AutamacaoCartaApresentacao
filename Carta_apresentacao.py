'''Automação de Carta Apresentação para vagas similares,
em que a mesma carta possa ser usada diversas vezes,
salvando arquivo em docx com nome da empresa e o cargo'''

from docx import Document
empresa = input('Qual nome da empresa?')
vaga = input('Qual nome da vaga?')

# Conteúdo da carta, segue exemplo inicial

carta = (
    f"Estou escrevendo para expressar meu interesse na posição de {vaga}. Com uma sólida "
    f"formação acadêmica em #####, complementada por um MBA em ##### "
    f"pela renomada #####, e uma trajetória profissional marcada por experiências "
    f"significativas em ####, acredito que minhas habilidades "
    f"e competências estão alinhadas com as responsabilidades e requisitos da vaga na {empresa}."
)
# Criar documento
document = Document()
document.add_paragraph(carta)

# Nome do arquivo
nome_arquivo = f"{empresa}_{vaga}.docx"

# Salvar documento
document.save(nome_arquivo)

print(f"Documento salvo como {nome_arquivo}")
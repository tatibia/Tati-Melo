class AnalisadorDeTexto:
    def __init__(self, texto):
        self.texto = texto
        self.palavras = texto.split()

    def palavras_selecionadas(self, palavras_desejadas):
        return [palavra for palavra in self.palavras if palavra.lower() in palavras_desejadas]

    def palavras_maiusculas_minusculas(self):
        maiusculas = [palavra for palavra in self.palavras if palavra.isupper()]
        minusculas = [palavra for palavra in self.palavras if palavra.islower()]
        return maiusculas, minusculas

    def total_letras(self):
        return len([char for char in self.texto if char.isalpha()])

    def total_caracteres(self):
        return len(self.texto)

# Testar a classe
analisador = AnalisadorDeTexto('Será que, no futuro , a minha IA assistente vai se comunicar com a sua IA assistente? Isso é, de certa forma, não haverá tanta comunicação direta? Quem interpreta melhor e define como serão as mensagens, tons, etc, será a máquina? Isso vai ajudar a diminuir conflitos ou apenas vai piorar as nossas relações?')

palavras_selecionadas = analisador.palavras_selecionadas(["futuro" , "assistente"])
print("Palavras selecionadas:", palavras_selecionadas)

maiusculas, minusculas = analisador.palavras_maiusculas_minusculas()
print("Palavras maiúsculas:", maiusculas)
print("Palavras minúsculas:", minusculas)

total_letras = analisador.total_letras()
print("Total de letras (sem considerar espaços):", total_letras)

total_caracteres = analisador.total_caracteres()
print("Total de caracteres:", total_caracteres)
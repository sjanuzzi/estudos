from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return[tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome}({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + ('(Concluída)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa')
    casa.add('Lavar Pratos')
    print(casa)

    casa.procurar('Lavar Pratos').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

    print(casa)
    print('----------------------------------------------------------')

    mercado = Projeto('Mercado')
    mercado.add('Comprar Frutas')
    mercado.add('Comprar Produto de Limpeza')
    mercado.add('Comprar Itens para Pizza')
    print(mercado)

    comprar_frutas = mercado.procurar('Comprar Frutas')
    comprar_frutas.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

    print(mercado)


if __name__ == '__main__':
    main()

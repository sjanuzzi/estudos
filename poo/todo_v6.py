from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return[tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome}({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencidas)')
            else:
                dias = (self.vencimento-datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)  # referenciando a classe tarefa
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', datetime.now())
    casa.add('Lavar Pratos', datetime.now() + timedelta(days=3, minutes=12))
    casa.add(TarefaRecorrente('Trocar lençois', datetime.now(), 7))
    casa.add(casa.procurar('Trocar lençois').concluir())
    print(casa)

    casa.procurar('Lavar Pratos').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)
    print('----------------------------------------------------------')

    mercado = Projeto('Mercado')
    mercado.add('Comprar Frutas', datetime.now())
    mercado.add('Comprar Produto de Limpeza',
                datetime.now() + timedelta(days=2, minutes=12))
    mercado.add('Comprar Itens para Pizza', datetime.now() +
                timedelta(days=4, minutes=12))
    mercado.tarefas.append(TarefaRecorrente('Comprar carne', datetime.now()))
    print(mercado)

    comprar_frutas = mercado.procurar('Comprar Frutas')
    comprar_frutas.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')

    print(mercado)


if __name__ == '__main__':
    main()
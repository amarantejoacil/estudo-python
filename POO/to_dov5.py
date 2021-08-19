#!/usr/local/bin/python3
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
        # in not tarefa.feito = se tarefa nao for feito

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]
        # possivel erro IndexError
        # 0 representa pega primeira desc que encontrou

    # imprimir objeto __repr__
    def __repr__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)'


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
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f' Vence em {dias} dias')
        return f'{self.descricao}' + ''.join(status)

# herenca atraves do super.
# utiliza metodo da pai e acrescenta algo a mais.


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()  # reuso de codigo
        # acrescentando novo comportamento
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', datetime.now())
    casa.add('Lavar Prato')
    casa.tarefas.append(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('Trocar lencois').concluir())
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, minutes=12))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()

    for tarefa in mercado:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()

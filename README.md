# Deadlock

_Trabalho de SO_


### **DESCRIÇÃO:**

Desenvolver um simulador para a detecção de Impasses
(Deadlocks). O seu simulador deve receber como entrada um arquivo padronizado de
acordo com o arquivo entrada.txt. Como resultado o simulador deve mostrar como resposta uma das
três opções a seguir:

1. Existe processos em Deadlock (2 processos ou mais);
    1. Imprimir quais os processos que estão em deadlock;
    2. Imprimir quantas instâncias de qual(is) recursos estão em falta em cada
processo;

2. Não existe processo em DeadLock
    1. Imprimir “Todos os processos foram finalizados”

3. Existe um único processo esperando por recursos externos;
    1. Imprimir qual o processo que está em espera;
    2. Imprimir quantas instâncias de qual(is) recursos estão em falta;

### **Informações adicionais:**

Você deve assumir que se existir recursos disponíveis para
um processo P qualquer, o mesmo irá obter esses recursos, irá executar e ao terminar

a execução irá devolver todos os recursos que estavam alocados para ele.

### **Informações adicionais 2:**

Seu simulador não precisa considerar a questão de estados
seguros e inseguros

(mas caso você queira implementar esse item fique à vontade).

### **EXEMPLO DE ARQUIVO DE ENTRADA**

```txt
3 4

4 2 3 1

2 1 0 0

0 0 1 0
2 0 0 1
0 1 2 0

2 0 5 1
1 0 1 0
2 1 0 0
```

### Explicação do Arquivo de Entrada.txt

- 3 4 → 3 Processos(P1, P2 e P3) e 4 Recursos (R1, R2 , R3 e R4)

- 4 2 3 1 → Vetor de Recursos Existentes

    4 Instâncias de R1,

    2 Instâncias de R2,

    3 Instâncias de R3,

    1 Instância de R4.

- 2 1 0 0 → Vetor de Recursos Disponíveis

    2 Instâncias disponíveis de R1,

    1 Instância disponível de R2,
    
    0 Instância disponível do R3,

    0 Instância disponível do R4.

- Matriz de alocação de recursos por Processo

    0 0 1 0 → P1 com 1 instância de R3
    
    2 0 0 1 → P2 com 2 instâncias de R1 e 1 instância de R4

    0 1 2 0 → P3 com 1 instância do R2 e 2 instâncias de R3

- Matriz de requisição de recursos por Processo

    2 0 5 1 → P1 requisitando 2 instâncias de R1, 5 de R3 e 1 de R4
    
    1 0 1 0 → P2 requisitando 1 instância de R1 e 3 de R3

    2 1 0 0 → P3 requisitando 2 instâncias de R1 e R2

**Para o Arquivo entrada.txt seu simulador deve imprimir na tela:**

    O processo P1 está em espera e aguardando 2 instâncias de R3
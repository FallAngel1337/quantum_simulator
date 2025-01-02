from collections import Counter
from gates import SingleQubit, MultipleQubits
from qubit import Qubit
import numpy as np

N_ITERATIONS = 100

class Circuit:
    def __init__(self, n):
        self.qubits = np.repeat(Qubit.zero(), n)
        self.n_iterations = 0
        self.queue = []
    
    # Operations
    def h(self, fst):
        self.queue.append(
            (SingleQubit.H, fst)
        )

    def cx(self, fst, snd):
        self.queue.append(
            (MultipleQubits.CX, fst, snd)
        )

    def add_operation(self, *ops):
        self.queue.extend(ops)

    def run(self, n_iterations):
        self.n_iterations = n_iterations

        for _ in range(n_iterations):
            qubits = self.qubits.copy()

            for step in self.queue:
                gate, index = step[0], list(step[1:])
                qubits[index] = gate(*qubits[index])
        
            yield tuple(map(lambda x: str(x.measure()), qubits))

    def results(self, run):
        for key, value in Counter(run).items():
            print(f'{str(key)}({value}): {value / self.n_iterations * 100}%')

c = Circuit(2)

c.h(0)
c.cx(0, 1)
c.results(c.run(N_ITERATIONS))

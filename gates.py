from qubit import Qubit
import numpy as np

H = np.sqrt(1/2) * np.array([
    [1, 1],
    [1, -1]
])

X = np.array([
    [0, 1],
    [1, 0]
])

Y = np.array([
    [0, -1j],
    [1j, 0]
])

Z = np.array([
    [1, 0],
    [0, -1]
])

S = np.array([
    [1, 0],
    #   vv -> e^(i^pi/2)
    [0, 1j]
])

T = np.array([
    [1, 0],
    #   vvvvvvvvvvvvvvvvvvvvvvvvvvvv -> e^(i*pi/4)
    [0, np.sqrt(2)/2 * complex(1, 1)]
])

class SingleQubit:
    @staticmethod
    def H(qubit: Qubit) -> Qubit:
        return Qubit(H @ qubit.amps)
    
    @staticmethod
    def X(qubit: Qubit) -> Qubit:
        return Qubit(X @ qubit.amps)
    
    @staticmethod
    def Y(qubit: Qubit) -> Qubit:
        return Qubit(Y @ qubit.amps)
    
    @staticmethod
    def Z(qubit: Qubit) -> Qubit:
        return Qubit(Z @ qubit.amps)
    
    @staticmethod
    def S(qubit: Qubit) -> Qubit:
        return Qubit(S @ qubit.amps)
    
    @staticmethod
    def T(qubit: Qubit) -> Qubit:
        return Qubit(T @ qubit.amps)
    
class MultipleQubits:
    def CTRL(control: Qubit, target: Qubit, gate) -> Qubit:
        return gate(target) if control.measure().is_one() else target
    
    def Toffoli(ctrl_1: Qubit, ctrl_2: Qubit, target: Qubit) -> Qubit:
        if ctrl_1.measure().is_one() and ctrl_2.measure().is_one():
            return SingleQubit.X(target)
        return target
    
    def CX(control: Qubit, target: Qubit) -> Qubit:
        return MultipleQubits.CTRL(control, target, SingleQubit.X)
    
    def CY(control: Qubit, target: Qubit) -> Qubit:
        return MultipleQubits.CTRL(control, target, SingleQubit.Y)
    
    def CZ(control: Qubit, target: Qubit) -> Qubit:
        return MultipleQubits.CTRL(control, target, SingleQubit.Z)

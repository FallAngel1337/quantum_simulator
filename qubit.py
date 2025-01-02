import numpy as np

class InvalidQubitAmplitudes(Exception):
    "Qubit amplitudes absolute square sum must add up to 1"

class Qubit:
    def __init__(self, amps: np.ndarray) -> None:
        self.is_collapsed = False
        # Note: need rounding due leading 2 (1.0000000000000002)
        if np.round(np.sum(np.abs(amps)**2)) == 1:
            self.amps = amps
        else:
            raise InvalidQubitAmplitudes

    @staticmethod
    def zero():
        return Qubit(np.array([1, 0]))
    
    @staticmethod
    def one():
        return Qubit(np.array([0, 1]))
    
    @staticmethod
    def random():
        rng = np.random.default_rng()
        angle = rng.random(1)[0]
        return Qubit([np.cos(angle), np.sin(angle)])
    
    def measure(self):
        if not self.is_collapsed:
            rng = np.random.default_rng()
            zero, one = Qubit.zero(), Qubit.one()
            probs = np.abs(self.amps)**2
            self.amps = rng.choice([zero.amps, one.amps], p=probs)
        self.is_collapsed = True
        return self

    def is_zero(self) -> bool:
        return self == Qubit.zero()
    
    def is_one(self) -> bool:
        return self == Qubit.one()

    def __eq__(self, other) -> bool:
        return self.amps[0] == other.amps[0] and self.amps[1] == other.amps[1]
    
    def __str__(self):
        if self.is_zero():
            return '|0>'
        if self.is_one():
            return '|1>'
        return f'Qubit({self.amps})'
    
    def __repr__(self):
        return f'Qubit(is_collapsed={self.is_collapsed}, amps={self.amps})'

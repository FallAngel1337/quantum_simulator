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
    

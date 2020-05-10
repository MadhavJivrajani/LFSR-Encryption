import numpy as np
from numpy.linalg import matrix_power

class LFSR:
    def __init__(self, n, count_type, seed):
        """
        n          : order of the minimal polynomial
                     will generalise later, trying with n = 5
        
        count_type : type of LFSR,
                     "fib": Fibonacci
                     "gal": Galois
                     Trying only fib for now
        seed       : Initial configuration of the LFSR
        """
        self.n = n
        self.type = -1
        if count_type == 'fib':
            self.type = 0
        elif count_type == 'gal':
            self.type = 1
        else:
            raise ValueError("Types of counters: 'fib' and 'gal'")
        
        self.companion = np.array([[0, 0, 0, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [0, 0, 0, 1, 0]])
        
        self.seed = np.array(seed)
        
    def __generate_next(self, state, k):
        if k < 0:
            raise ValueError("Power of matrix needs to be non-negative")
        else:
            return np.mod(matrix_power(state, k), 2) #remove the mod to generate non-binary vectors
        
        
    def get_max_period(self):
        return 2**self.n - 1
    
    def print_states(self):
        for k in range(self.get_max_period()):
            temp = self.__generate_next(self.companion, k)
            new_state = np.dot(temp, self.seed)
            print(" ".join([str(i) for i in list(new_state)]))

            
lfsr = LFSR(5, 'fib', [0, 0, 0, 0, 1])
lfsr.print_states()

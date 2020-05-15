import numpy as np
from numpy.linalg import matrix_power
from feedback import feedback_poly, one_hot_encode

class LFSR:
    def __init__(self, n, count_type, seed):
        """
        n          : order of the minimal polynomial        
        count_type : type of LFSR,
                     "fib": Fibonacci
                     "gal": Galois
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
        
        if self.type == 0:
            self.companion = self.__generate_companion_fibonacci()
        else:
            self.companion = self.__generate_companion_galois()

        self.seed = np.array(seed)
    
    def __generate_companion_galois(self):
        diag = np.diag(np.ones(self.n - 1, dtype=np.int32))
        zeros = np.zeros(self.n - 1, dtype=np.int32)
        temp = np.vstack((diag, zeros))
        return np.mod(np.column_stack((np.array(
            one_hot_encode(self.n)[::-1]), temp)), 2)

    def __generate_companion_fibonacci(self):
        diag = np.diag(np.ones(self.n - 1, dtype=np.int32))
        zeros = np.zeros(self.n - 1, dtype=np.int32)
        temp = np.column_stack((zeros, diag))
        return np.mod(np.vstack(
            (temp, np.array(one_hot_encode(self.n)))), 2)
        
    def __generate_next(self, state, k):
        if k < 0:
            raise ValueError("Power of matrix needs to be non-negative")
        else:
            return np.mod(matrix_power(state, k%(self.get_max_period())), 2)
        
    def get_max_period(self):
        return 2**self.n - 1
    
    def encrypt_decrypt_ints(self):
        ints = []
        for k in range(self.get_max_period()):
            temp = self.__generate_next(self.companion, k)
            new_state = np.array(np.mod(np.dot(temp, self.seed), 2), dtype=np.int32)
            ints.append(int("".join([str(int(i)) for i in list(new_state)]), 2)%255)
        
        return np.array(ints)

    def get_ints(self):
        ints = []
        for k in range(self.get_max_period()):
            temp = self.__generate_next(self.companion, k)
            new_state = np.array(np.mod(np.dot(temp, self.seed), 2), dtype=np.int32)
            ints.append(int("".join([str(int(i)) for i in list(new_state)]), 2))
        
        return np.array(ints)
    
    def generate_output_stream(self):
        stream = []
        if self.type == 0:
            for k in range(self.get_max_period()):
                temp = self.__generate_next(self.companion, k)
                new_state = np.mod(np.dot(temp, self.seed), 2)
                stream.append(new_state[-1])
        else:
            for k in range(self.get_max_period()):
                temp = self.__generate_next(self.companion, k)
                new_state = np.mod(np.dot(temp, self.seed), 2)
                stream.append(new_state[0])
                
        return np.array(stream)
            
    def print_states(self):
        for k in range(self.get_max_period()):
            temp = self.__generate_next(self.companion, k)
            new_state = np.mod(np.dot(temp, self.seed), 2)
            print(" ".join([str(int(i)) for i in list(new_state)]))

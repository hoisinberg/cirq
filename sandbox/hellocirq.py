import cirq

# Declare a qubit intialized to thd |0> state
q = cirq.NamedQubit('q')

# Circuits include information about hardware constraints
# For now, use a free circuit
c = cirq.Circuit()

# Instruct the circuit to perform an operation
c.append(cirq.H(q))

# Create a simulator
s = cirq.Simulator()

# Classically computes the resulting wavefunction
print(s.simulate(c))

# Instruct the circuit to perform a measurement
c.append(cirq.measure(q, key = 'result'))

# Simulate measurement outcomes using the computed probabilities
print(s.run(c, repetitions=1000).histogram(key='result'))



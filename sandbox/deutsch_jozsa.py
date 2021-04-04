import cirq
from typing import List

def deutsch_josza(
  qubits: List['cirq.Qid'],
  circuit: 'cirq.Circuit',
  oracle_op: cirq.OP_TREE):

  n = len(qubits) - 1

  circuit.append(cirq.X(qubits[n]))
  circuit.append(cirq.H(qubits[n]))

  for i in range(n):
    circuit.append(cirq.H(qubits[i]))

  circuit.append(oracle_op)

  for i in range(n):
    circuit.append(cirq.H(qubits[i]))

def const_zero(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
  return []

def const_one(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
  return cirq.X(qubits[len(qubits) - 1])

def balanced_parity(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
  n = len(qubits) - 1
  return [cirq.CX(qubits[i], qubits[n]) for i in range(n)]

def balanced_mod2(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
  return cirq.CX(qubits[0], qubits[len(qubits) - 1])

def main():
  n = 3
  qubits = cirq.LineQubit.range(n + 1)
  circuit = cirq.Circuit()

  deutsch_josza(qubits, circuit, balanced_parity(qubits))

  # Create a simulator
  s = cirq.Simulator()

  # Classically computes the resulting wavefunction
  print(s.simulate(circuit))

  # Instruct the circuit to perform a measurement
  circuit.append(cirq.measure(*qubits[0:n], key = 'result'))

  # Simulate measurement outcomes using the computed probabilities
  print(s.run(circuit, repetitions = 1000).histogram(key = 'result'))

if __name__ == "__main__":
  main()
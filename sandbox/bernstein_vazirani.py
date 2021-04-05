import cirq
from typing import List

def bernstein_vazirani(
  qubits: List[cirq.Qid],
  circuit: cirq.Circuit,
  s: List[bool]) -> None:

  n = len(s)
  oracle_op = create_oracle(s)
  circuit.append(cirq.X(qubits[n]))
  circuit.append(cirq.H(qubits[n]))
  circuit.append(hadamard(qubits))
  circuit.append(oracle_op(qubits))
  circuit.append(hadamard(qubits))


def hadamard(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
  n = len(qubits) - 1
  return [cirq.H(qubits[i]) for i in range(n)]

def create_oracle(s: List[bool]):
  def oracle_op(qubits: List[cirq.Qid]) -> cirq.OP_TREE:
    if len(qubits) != len(s) + 1:
      raise ValueError(f'{len(qubits)} qubits passed to oracle expecting {len(s) + 1}')
  
    n = len(qubits) - 1
    return [cirq.CX(qubits[i], qubits[n]) for i in range(n) if s[i]]

  return oracle_op


def main():
  n = 8
  qubits = cirq.LineQubit.range(n + 1)
  circuit = cirq.Circuit()

  bernstein_vazirani(qubits, circuit, [True, True, False, False, True, False, False, True])

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
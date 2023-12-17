import qiskit

versions = qiskit.__qiskit_version__
for key, value in versions.items():
    print("{}: {}".format(key, value))
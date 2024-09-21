
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
def func_a():
    pass
def func_b():
    func_a()
def main():
    func_b()
with PyCallGraph(output=GraphvizOutput()):
    main()
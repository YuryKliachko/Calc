import runpy

def run():
    runpy.run_module('calc.gui', run_name='__main__')

if __name__ == "__main__":
    run()
import runpy
import click

@click.command()
@click.argument('console', required=False)
def run(console):
    if console:
        runpy.run_module('calc.console')
    else:
        runpy.run_module('calc.gui', run_name='__main__')

if __name__ == "__main__":
    run()
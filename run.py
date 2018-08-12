import runpy
import click

@click.command()
@click.argument('console', required=False)
def run(console):
    if console:
        runpy.run_module('calc.console')
    else:
        runpy.run_module('calc.gui', run_name='__main__')
# Some comments here
# One more comment
if __name__ == "__main__":
    run()
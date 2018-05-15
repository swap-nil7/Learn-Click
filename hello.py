import click

class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose

@cli.command()
@click.option('--string', default='World',
              help='This is the thing that is greeted')
@click.option('--repeat', default=1,
              help='The number of times to be greeted')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
@pass_config
def greet(config, string, repeat, out):
    '''This is a script to greet'''
    if config.verbose:
        click.echo('swap_it')
    for i in xrange(repeat):
        click.echo('Hello {}'.format(string), file=out)


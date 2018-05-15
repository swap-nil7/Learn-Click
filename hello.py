import click

@click.command()
@click.option('--string', default='World',
              help='This is the thing that is greeted')
@click.option('--repeat', default=1,
              help='The number of times to be greeted')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
def cli(string, repeat, out):
    '''This is a script to greet'''
    for i in xrange(repeat):
        click.echo('Hello {}'.format(string), file=out)


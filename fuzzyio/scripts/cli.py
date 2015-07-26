# Skeleton of a CLI

import click

import fuzzyio


@click.command('fuzzyio')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(fuzzyio.has_legs)

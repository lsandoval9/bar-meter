import json
import click

from listening_server import start_server


@click.command("hello")
@click.version_option("0.1.0", prog_name="BER meter")
def start():
    click.echo("Hello, World!")

    start_server()


def function1():
    print("Function 1 called")

def function2():
    print("Function 2 called")

def function3():
    print("Function 3 called")

def main():
    start(prog_name="cli")


if __name__ == "__main__":
    main()

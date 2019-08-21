#!/usr/bin/python
import numpy
import click
import pandas
import re

import scipy.signal as signal
import PIL.Image as Image

from matplotlib import pyplot as plt


@click.command()
@click.option(
    "--input_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        allow_dash=False,
        path_type=None,
    ),
    required=True,
)
@click.option(
    "--output_path",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        readable=True,
        resolve_path=True,
        allow_dash=False,
        path_type=None,
    ),
    required=True,
)
@click.option("--window_size", required=False, type=click.STRING, default="3,3")
@click.option("--dpi", required=False, type=click.IntRange(200, 2400), default=200)
def run(input_path, output_path, window_size, dpi):
    click.echo("Filtering data...")
    input_file = open(input_path, "r")
    csv_as_array = numpy.genfromtxt(input_file, delimiter=",")

    filtered_array = signal.medfilt2d(
        csv_as_array, kernel_size=list(map(int, window_size.split(",")))
    )

    output_file = open(f"{strip_csv(output_path)}-filtered.csv", "w+")
    frame = pandas.DataFrame(filtered_array)
    frame.to_csv(output_file)

    click.echo("Creating images...")
    bplot = plt.imshow(csv_as_array)

    plt.colorbar()
    plt.savefig(
        f"{strip_csv(output_path)}-unfiltered.jpg",
        bbox_inches="tight",
        format="jpg",
        dpi=dpi,
    )

    plt.clf()

    aplot = plt.imshow(filtered_array)
    plt.colorbar()

    plt.savefig(
        f"{strip_csv(output_path)}-filtered.jpg",
        bbox_inches="tight",
        format="jpg",
        dpi=dpi,
    )

    plt.clf()
    click.echo(f"Finished filtering data...")
    click.echo(f"Filtered data: {strip_csv(output_path)}-filtered.csv")
    click.echo(f"Unfiltered image: {strip_csv(output_path)}-unfiltered.jpg")
    click.echo(f"Filtered image: {strip_csv(output_path)}-filtered.jpg")

    return f"{strip_csv(output_path)}-filtered"


def strip_csv(input_string):
    return re.sub(r".csv", "", input_string)


if __name__ == "__main__":
    output = run()
    click.echo(f"Location: {output}")

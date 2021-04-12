import argparse
from argparse import Namespace


def cmdLineParser() -> Namespace:

    parser = argparse.ArgumentParser(
        prog="Git Commit Exploder",
        usage="Program which checkouts all previous versions of a Git repository and stores them in a `../temp/` directory",
    )

    parser.add_argument(
        "-u",
        "--url",
        nargs=1,
        default="https://github.com/SoftwareSystemsLaboratory/Metrics-Dashboard.git",
        type=str,
        required=True,
        help="The Git repository URL.",
    )

    parser.add_argument(
        "-s",
        "--src",
        nargs=1,
        type=str,
        default="Metrics-Dashboard",
        required=True,
        help="The name of the Git repository. Must match the name of whatever the root folder of the Git repository is after executing 'git clone'.",
    )

    parser.add_argument(
        "--start",
        nargs=1,
        default=1,
        type=int,
        required=True,
        help="Allows for the downloading of hash codes to start with a hash code later than the first one. If left unspecified it is automatically set to 1 and every hash code is included.",
    )

    parser.add_argument(
        "--stride",
        nargs=1,
        default=0,
        type=int,
        required=True,
        help="Allows you to skip every n hash codes. When used in conjunction with the start command it allows for the downloading of each hash to be spread more easily between compute nodes.",
    )

    return parser.parse_args()

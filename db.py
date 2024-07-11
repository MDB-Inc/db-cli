#!/usr/bin/env python3
from argparse import Namespace

from modules.args import get_argument_parser
from modules.run import run_command


if __name__ == '__main__':
    parser = get_argument_parser()
    args: Namespace = parser.parse_args()
    run_command(args)

import argparse
from argparse import RawTextHelpFormatter
import os
import sys

# Welcome to Peek!
# This is a peak finding tool for usage in motif enrichment analysis.
# It outputs a HOMER-style peaks.txt file.
# From HOMER website:

def main():
    parser = argparse.ArgumentParser(
        prog="peek",
        description="Command line tool to find peaks in ChIP-Seq data."
    )


    # Input
    parser.add_argument("chip", help="ChIP data file", type=str)




    # Parse args
    args = parser.parse_args()


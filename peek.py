import argparse
import os
import sys

# Welcome to Peek!
# This is a peak finding tool for usage in motif enrichment analysis.
# It outputs a peaks.txt file.
# From HOMER website:
#   Column 1: PeakID - a unique name for each peak (very important that peaks have unique names...)
#   Column 2: chr - chromosome where peak is located
#   Column 3: starting position of peak
#   Column 4: ending position of peak
#   Column 5: Strand (+/-)
#   Column 6: Normalized Tag Counts - number of tags found at the peak, normalized to 10 million total mapped tags (or defined by the user)
#   Column 7: (-style factor): Focus Ratio - fraction of tags found appropriately upstream and downstream of the peak center. (see below)
#                 (-style histone/-style groseq): Region Size - length of enriched region
#   Column 8: Peak score (position adjusted reads from initial peak region - reads per position may be limited)
#   Columns 9+: Statistics and Data from filtering


def peek(file_path, threshold):
    try:
        with open(file_path, 'r') as file:
            peaks = []
            for line in file:
                parts = line.strip().split()

parser = argparse.ArgumentParser(
    prog="peek",
    description="Command line tool to find peaks in ChIP-Seq data."
    )


# Input
parser.add_argument("chip", help="ChIP data file", type=str)




# Parse args
args = parser.parse_args()


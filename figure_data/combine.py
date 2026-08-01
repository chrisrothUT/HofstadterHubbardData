#!/usr/bin/env python3

import argparse
import sys

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="Input .npy files")
    args = parser.parse_args()

    arrays = [np.asarray(np.load(path)).ravel() for path in args.files]

    lengths = [len(array) for array in arrays]
    if len(set(lengths)) != 1:
        raise ValueError(f"Arrays have different lengths: {lengths}")

    data = np.column_stack(arrays).real

    np.savetxt(
        sys.stdout,
        data,
        delimiter="\t",
        fmt="%.10g",
    )


if __name__ == "__main__":
    main()

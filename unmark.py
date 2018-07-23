"""Remove unneccessary MarkDown and text from GodMode9 README."""

__author__ = "Death Mask Salesman"
__copyright__ = "Copyright 2018, Death Mask Salesman"
__license__ = "BSD-3-Clause"
__version__ = "0.1"

import argparse
import gzip
import json
import os
import re

ap = argparse.ArgumentParser(
        description="Scrubber for GodMode9's README.md file."""
)

ap.add_argument(
        "input",
        type=str,
        help="the README.md file"
)
ap.add_argument(
        "output",
        type=str,
        help="where to save the modified README.md"
)


def load_patch(patch_path):
    """Reads the patch data if any."""

    try:
        with gzip.open(patch_path, "rb") as f:
            patch_data = json.load(f)
    except BaseException:
        # Corrupted or non-existent patch file
        patch_data = []

    return patch_data


def apply_patch(patch_data, data):
    """Replaces content in data if present in patch_data."""

    unmatched = []

    for pattern in patch_data:
        if data.find(pattern[0]) == -1:
            unmatched.append(pattern[0])
        else:
            data = data.replace(pattern[0], pattern[1])

    for pattern in unmatched:
        print("Warning: pattern not found: {0!r}".format(pattern))

    return data


def strip_md(data):
    """Removes certain MarkDown from line."""

    # NOTE: list a two-char string before its single-char equivalent
    #       (i.e. ["__", "_"] ok, ["_", "__"] NOT ok)
    # Omitting "`" for now
    blacklist = ["__", "**", "\\"]

    for pattern in blacklist:
        data = data.replace(pattern, "")

    return data


def replace_links(data):
    """Replaces links with their corresponding anchor text."""

    # Identify any link in the format [anchor](URL)
    for pair in re.findall("\[(.*?)\]\((.*?)\)", data):
        pattern = "[{0}]({1})".format(pair[0], pair[1])

        # And replace them
        data = data.replace(pattern, pair[0])

    return data


def main(src, dst):
    """Core of Unmark."""

    # Safety measure
    if os.path.exists(dst):
        print("Fatal: {0} already exists.".format(dst))
        exit(1)

    try:
        with open(src, "r") as f:
            data = f.read()
    except BaseException as e:
        print("Fatal: {0}.".format(e))
        exit(1)

    unmark_dir = os.path.dirname(os.path.abspath(__file__))
    patch_path = "{0}/patch.json.gz".format(unmark_dir)

    # Load the JSON containing patterns and replacements
    patch_data = load_patch(patch_path)
    if not patch_data:
        print("Warning: patch not found or corrupted.")
    else:
        # And apply the replacements
        data = apply_patch(patch_data, data)

    # Strip away unused MD, then replace links with anchor texts
    data = strip_md(data)
    data = replace_links(data)

    # Dump it all to the ReadMe to be baked into GM9
    try:
        with open(dst, "w") as f:
            f.write(data)
    except BaseException as e:
        print("Fatal: {0}.".format(e))


if __name__ == "__main__":
    args = ap.parse_args()

    main(args.input, args.output)

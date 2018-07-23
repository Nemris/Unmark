# Unmark

Unmark is a CLI tool aimed at producing a README.md file suitable for use as
[GodMode9][1] embedded user guide. It achieves this goal by scrubbing away
any useless MarkDown syntax, replacing links with their matching anchor text
and applying a number of text replacements read from a `patch.json.gz` file.

-----

## Requirements

To run Unmark, you need **Python >= 3.5**.

-----

## Installation

No installation procedure is needed; simply clone or download the repository.

-----

## Usage

Unmark is ran by means of:

    python unmark.py src dst

Where `src` is the original README.md file, and `dst` is the new file.
Precautions are taken so that already existent files are not overwritten, thus
Unmark will halt in such a case.

-----

## Workflow

A typical run consists of the following steps:

 * Opening the input file;
 * Checking for a `patch.json.gz` file in the same path as the script;
 * Applying the replacements elencated in the abovementioned file;
 * Scrubbing any MarkDown that renders to bold text, alongside backslashes;
 * Replacing links with the corresponding anchor text;
 * Writing the modified data to a new file.

-----

## The `patch.json.gz` file

This file is a `gzip`ped JSON database, containing a list of lists. Each nested
list contains the pattern to be matched, and the data to replace the pattern
with. This allows for precise adjustments of the README.md file, from replacing
parts of a sentence to deleting whole lines.

Unmark will warn in case this file is missing, or in case one of the patterns
within it cannot be matched. It is generally not recommended to run Unmark
without said database.

To edit `patch.json.gz`, unpack it with `gzip -d` first. Once you're done,
repack it with `gzip`.

-----

## License

This tool is licensed under the terms of the BSD-3-Clause license. See the
`LICENSE` file for additional details.

[1]: https://github.com/d0k3/GodMode9

# unmark

`unmark` is a CLI tool aimed at producing a `README.md` file suitable for use as [GodMode9][1] embedded user guide.

It achieves this goal by scrubbing away any unneeded MarkDown syntax, replacing links with their matching anchor text and applying a number of text replacements read from a `patch.json.gz` file.

-----

## Requirements

To run `unmark`, you need **Python >= 3.5**.

-----

## Installation

No installation procedure is needed; simply clone the repository, or download `unmark.zip` from the latest release.

-----

## Usage

You can use:

    python unmark.py -h

To display the following usage message:

    usage: unmark.py [-h] [-f] src dst
    
    Create an user manual from GodMode9's README.md file.
    
    positional arguments:
      src          the original README.md file
      dst          the user manual
    
    optional arguments:
      -h, --help   show this help message and exit
      -f, --force  overwrite the output file, if present

Specifying an already existing file as `dst` will halt the script; if you don't care about the file, pass `-f` to overwrite it.


-----

## Workflow

Once started, `unmark` will perform the following:

 1. open the input file;
 2. load a `patch.json.gz` file located in the same directory as the script;
 3. perform the replacements dictated by `patch.json.gz`, report any unmatched pattern;
 4. scrub any unneeded MarkDown;
 5. replace links with the corresponding anchor text;
 6. write the modified data to a new file.

Any errors during steps 1 and 6 are treated as fatal errors.

Any errors during steps 2 and 3 are treated as warnings.

-----

## The `patch.json.gz` file

This file is a `gzip`ped JSON database, containing a list of lists.
Each nested list contains the pattern to be matched, and the data to replace the pattern
with.
This allows for precise adjustments of the README.md file, from replacing parts of a sentence to deleting whole lines.

`unmark` will warn in case this file is missing, or in case one of the patterns within it cannot be matched.
It is generally not recommended to run `unmark`
without said database.

To edit `patch.json.gz`, unpack it with `gzip -d` first. Once you're done, repack it with `gzip`.

-----

## License

This tool is licensed under the terms of the BSD-3-Clause license. See the
`LICENSE` file for additional details.

[1]: https://github.com/d0k3/GodMode9

# Goobertown Roulette STL Selector

**_Important_** This is a Python script and will require an interpreter to execute. In other words, it's not a program that can be downloaded and run by itself.

A simple file selector made in Python to allow a random selection of 3D printable STL files for participation in the Goobertown Roulette game from the YouTube channel Goobertown Hobbies.

## Usage

The script simply makes a random selection out of all STL files in a directory you supply, including those in subfolders. You will be able to run it several times in a row in case you're like me and simply run it over a whole library which may return bases, weapons, terrain, or other non-character files. 

Be careful running the script over a large file structure as it may take a long time and consume a lot of resources. As a sample benchmark, it takes me ~1.2 seconds to scan and select from the entire current (2020-11-06) Artisan Guild catalogue (1842 files). Your performance will vary.

## Future Additions

This is a work in progress. I intend on adding features as I am able, though there is no given timeline or promise of completion.

- Inclusion of rules for each season and the ability to select randomly from them to deliver a complete challenge package.
- A registry of folders to be scanned so the program will require less input.
- An optional registry of files that have been previously selected to avoid duplicates or useless files.

I also realize that Python is a barrier to entry for many people as it is not a file that can simply be be downloaded and ran on any machine, it's simply my fastest and most comfortable language for a proof of concept. Eventually I would like to provide a compiled version that can be downloaded and executed natively without an interpreter.

## Testing

This script has been tested using Python 3.8 on Windows 10 and Ubuntu 2020.04.

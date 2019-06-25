# PDF Stamper using pdftk library

This python script batch stamps/watermarks pdf documents.

### NOTE: Save this script in it's dedicated folder. The folder should only contain this script.

The script can do stamp and multistamp.

**stamp** - Stamp all pages of one pdf with corresponding stamp pdf file. Enter full paths to folder of to be stamped files, folder containing stamp files and output folder.
        Filenames must start with 3 characters corresponding to the stamp filename you want to stamp with.
        Example Filenames:
                    To be stamped file: 001-abc.pdf
                    Stamp file: 001-xyz.pdf

**multistamp** - Stamp all pages of all files with one stamp.pdf. Enter full path to folder containing to be stamped files, full path to stamp FILE and output folder.
             The stamp file need not have follow the naming convention as described in stamp.

### NOTE: The stamps have to be pdf documents containing the data you want to stamp.

Check documentation @ https://www.pdflabs.com/docs/pdftk-man-page/

#### Dependencies:

You need to install `pdftk` for this script to run. You can install it using
the following commands in the terminal:

    $ sudo add-apt-repository ppa:malteworld/ppa
    $ sudo apt update
    $ sudo apt install pdftk

You can find the repository for more information at: https://gitlab.com/pdftk-java/pdftk

#### Usage:

    $ python3 pdf_stamper.py

#### To make the script executable from terminal, enter in terminal:

    $ chmod u+x /path/to/file

#### Then use the following command to run the script from it's directory:

    $ ./pdf_stamper.py
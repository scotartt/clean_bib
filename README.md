#clean_bib.py - Delete Unwanted Bibliography fields from .bib files.

Do you use Mendeley, Papers, Zotero or other bibliographic softwares that export their bibliography to bibtex .bib files for use in Latex with with bibTeX or bibLaTeX?

Do you hate the way those bibliographic softwares generally export a .bib file that can’t exclude certain fields that make a total hash of your Bibliography Entries?

This Python script is for you! It deletes the extraneous fields in the .bib file leaving you with just the essential ones, like Author, Year, Title, Journal, etc. 

##Installing the script

You will need Python 3. I use Python 3.3 - I haven’t checked if this works with Python 2.x. In fact I know it won’t. Use Python 3 or convert it to Python 2 yourself.

You will also need the super-excellent [BibTexParser project](https://bibtexparser.readthedocs.org/en/latest/index.html) installed into your Python environment. If you don’t have that installed, install like this:

    pip install bibtexparser

Otherwise see the instructions on the linked page above if you don’t/can’t/won’t use pip.

##Using the script

Currently the script is hard-coded to read “library.bib” from the current directory and write to “library_clean.bib” in the current directory. I will shortly make this configurable. In the meantime edit these lines:

    input_b = "library.bib"
    output_b = "library_clean.bib"

To run the script, on the command line, type:

    python clean_bib.py

##Customising what fields are removed

It works by removing fields you don’t want, and leaving any others. You can customise what fields are removed by editing the line:

    unwanted = ["doi", "url", "abstract", "file", "isbn", "link", "keyword", "mendeley-tags", "annote", "pmid", "chapter", "institution", "issn", "month"]

Just add any fields you don’t want to this Python list. If you a field, e.g. doi, url, isbn etc, then remove it from the list.

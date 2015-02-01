import datetime
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import *

input_b = "library.bib"
output_b = "library_clean.bib"

now = datetime.datetime.now()
print("{0} Cleaning duff bib records from {1} into {2}".format(now, input_b, output_b))

# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library
    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = page_double_hyphen(record)
    record = convert_to_unicode(record)
    ## delete the following keys.
    unwanted = ["doi", "url", "abstract", "file", "gobbledegook", "isbn", "link", "keyword", "mendeley-tags", "annote", "pmid", "chapter", "institution", "issn", "month"]
    for val in unwanted:
        record.pop(val, None)
    return record


bib_database = None
with open(input_b) as bibtex_file:
    parser = BibTexParser()
    parser.customization = customizations
    parser.ignore_nonstandard_types = False
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

if bib_database :
    now = datetime.datetime.now()
    success = "{0} Loaded {1} found {2} entries".format(now, input_b, len(bib_database.entries))
    print(success)
else :
    now = datetime.datetime.now()
    errs = "{0} Failed to read {1}".format(now, input_b)
    print(errs)
    sys.exit(errs)

bibtex_str = None
if bib_database:
    writer = BibTexWriter()
    writer.order_entries_by = ('author', 'year', 'type')
    bibtex_str = bibtexparser.dumps(bib_database, writer)
    #print(str(bibtex_str))
    with open(output_b, "w") as text_file:
        print(bibtex_str, file=text_file)

if bibtex_str:
    now = datetime.datetime.now()
    success = "{0} Wrote to {1} with len {2}".format(now, output_b, len(bibtex_str))
    print(success)
else:
    now = datetime.datetime.now()
    errs = "{0} Failed to write {1}".format(now, output_b)
    print(errs)
    sys.exit(errs)

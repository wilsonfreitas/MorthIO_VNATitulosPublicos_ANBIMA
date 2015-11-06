# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

from textparser import PortugueseRulesParser

class PortugueseRulesParser2(PortugueseRulesParser):
    def parseDate_ptBR(self, text, match):
        r'(\d{2})/(\d{2})/(\d{4})'
        return '{}-{}-{}'.format(match.group(3), match.group(2), match.group(1))

pp = PortugueseRulesParser2()
# Read in a page
html = scraperwiki.scrape("http://www.anbima.com.br/vna/vna.asp")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)

sel = "div#listaNTN-B > center > table > tr:nth-child(2) > td:nth-child(2)"
date = root.cssselect(sel)[0].text_content()
sel = "div#listaNTN-B > center > table > tr:nth-child(4) > td:nth-child(2)"
value = root.cssselect(sel)[0].text_content()

scraperwiki.sqlite.save(
    unique_keys=['data_ref', 'titulo'],
    data={
        "data_ref": pp.parse(date),
        "titulo": "NTNB",
        "VNA": pp.parse(value)
    })

sel = "div#listaNTN-C > center > table > tr:nth-child(2) > td:nth-child(2)"
date = root.cssselect(sel)[0].text_content()
sel = "div#listaNTN-C > center > table > tr:nth-child(4) > td:nth-child(2)"
value = root.cssselect(sel)[0].text_content()

scraperwiki.sqlite.save(
    unique_keys=['data_ref', 'titulo'],
    data={
        "data_ref": pp.parse(date),
        "titulo": "NTNC",
        "VNA": pp.parse(value)
    })

sel = "div#listaLFT > center > table > tr:nth-child(2) > td:nth-child(2)"
date = root.cssselect(sel)[0].text_content()
sel = "div#listaLFT > center > table > tr:nth-child(4) > td:nth-child(2)"
value = root.cssselect(sel)[0].text_content()

scraperwiki.sqlite.save(
    unique_keys=['data_ref', 'titulo'],
    data={
        "data_ref": pp.parse(date),
        "titulo": "LFT",
        "VNA": pp.parse(value)
    })

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

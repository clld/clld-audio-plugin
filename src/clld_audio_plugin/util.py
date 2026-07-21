"""
Utilities
"""
import re
from typing import Optional

from pycldf import Dataset
from csvw import Table, URITemplate
from csvw.datatypes import anyURI

__all__ = ['form2audio']


def get_url(ds: Dataset, table: Table, row: dict, url_template: Optional[URITemplate] = None):
    """Get the most appropriate URL for a row in MediaTable."""
    if url_template:
        res = url_template.expand(row)
    else:
        res = anyURI.to_string(ds.get_row_url(table, row))
    return re.sub(r'\w//', '/', res)


def form2audio(cldf: Dataset, mimetype: str = 'audio/mpeg') -> dict[str, str]:
    """
    Get suitable audio files for forms.

    If MediaTable has a pathInZip property, URL templates specified as valueUrl om the table's
    id column are preferred, since zip file members cannot really be linked to.

    The link between FormTable and MediaTable can be established in two ways:
    - MediaTable can be augmented with a formReference column,
    - FormTable can be augmented with a list-valued mediaReference column.

    :return: `dict` mapping form ID to audio file URL.
    """
    res = {}
    table = 'MediaTable' if 'MediaTable' in cldf else 'media.csv'
    with_media_type = (table, 'mediaType') in cldf
    props = ['mediaType'] if with_media_type else []

    url_template = None
    if ('MediaTable', 'pathInZip') in cldf:
        idcol = cldf['MediaTable', 'id']
        if idcol.valueUrl:
            url_template = idcol.valueUrl

    if (('MediaTable', 'formReference') in cldf) or (('media.csv', 'formReference') in cldf):
        for r in cldf.iter_rows(table, 'id', 'formReference', 'mediaType', *props):
            if r['mediaType' if with_media_type else 'mimetype'] == mimetype:
                res[r['formReference']] = get_url(cldf, table, r, url_template)
    else:
        assert ('FormTable', 'mediaReference') in cldf
        media = {r['id']: r for r in cldf.iter_rows('MediaTable', 'id', 'mediaType')}
        for f in cldf.iter_rows('FormTable', 'id', 'mediaReference'):
            for mid in f['mediaReference']:
                if media[mid]['mediaType'] == mimetype:
                    res[f['id']] = get_url(cldf, 'MediaTable', media[mid], url_template)

    return res

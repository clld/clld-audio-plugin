"""
Utilities
"""
from pycldf import Dataset

__all__ = ['form2audio']


def form2audio(cldf: Dataset, mimetype: str = 'audio/mpeg') -> dict[str, str]:
    """
    Get suitable audio files for forms.

    The link between FormTable and MediaTable can be established in two ways:
    - MediaTable can be augmented with a formReference column,
    - FormTable can be augmented with a list-valued mediaReference column.

    :return: `dict` mapping form ID to audio file URL.
    """
    res = {}
    table = 'MediaTable' if 'MediaTable' in cldf else 'media.csv'
    with_media_type = (table, 'mediaType') in cldf
    props = ['mediaType'] if with_media_type else []
    if (('MediaTable', 'formReference') in cldf) or (('media.csv', 'formReference') in cldf):
        for r in cldf.iter_rows(table, 'id', 'formReference', 'mediaType', *props):
            if r['mediaType' if with_media_type else 'mimetype'] == mimetype:
                res[r['formReference']] = cldf.get_row_url(table, r)
    else:
        assert ('FormTable', 'mediaReference') in cldf
        media = {r['id']: r for r in cldf.iter_rows('MediaTable', 'id', 'mediaType')}
        for f in cldf.iter_rows('FormTable', 'id', 'mediaReference'):
            for mid in f['mediaReference']:
                if media[mid]['mediaType'] == mimetype:
                    res[f['id']] = cldf.get_row_url('MediaTable', media[mid])

    return res

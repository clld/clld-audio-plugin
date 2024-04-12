__all__ = ['form2audio']


def form2audio(cldf, mimetype='audio/mpeg'):
    """
    Read a media table augmented with a formReference column.

    :return: `dict` mapping form ID to audio file.
    """
    res = {}
    table = 'MediaTable' if 'MediaTable' in cldf else 'media.csv'
    with_mediaType = (table, 'mediaType') in cldf
    props = ['mediaType'] if with_mediaType else []
    for r in cldf.iter_rows(table, 'id', 'formReference', 'mediaType', *props):
        if r['mediaType' if with_mediaType else 'mimetype'] == mimetype:
            res[r['formReference']] = cldf.get_row_url(table, r)
    return res

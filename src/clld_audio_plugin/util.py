__all__ = ['form2audio']


def form2audio(cldf, mimetype='audio/mpeg'):
    """
    Read a media table augmented with a formReference column.

    :return: `dict` mapping form ID to audio file.
    """
    res = {}
    for r in cldf.iter_rows('media.csv', 'id', 'formReference'):
        if r['mimetype'] == mimetype:
            res[r['formReference']] = cldf.get_row_url('media.csv', r)
    return res

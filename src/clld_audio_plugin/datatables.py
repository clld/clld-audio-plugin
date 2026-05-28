"""
Audioplayer column for form tables.
"""
from clld.web.datatables.base import Col
from clld.web.util.htmllib import HTML

__all__ = ['AudioCol']


class AudioCol(Col):
    """Audioplayer column."""
    __kw__ = {'bSearchable': False, 'bSortable': False}

    def format(self, item):  # pylint: disable=C0116
        if item.audio:
            return HTML.audio(
                HTML.source(src=item.audio, type="audio/mpeg"),
                controls="controls",
                preload="metadata"
            )
        return ''

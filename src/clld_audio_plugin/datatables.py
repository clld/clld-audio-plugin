from clld.web.datatables.base import Col
from clld.web.util.htmllib import HTML

__all__ = ['AudioCol']


class AudioCol(Col):
    __kw__ = dict(bSearchable=False, bSortable=False)

    def format(self, item):
        if item.audio:
            return HTML.audio(
                HTML.source(src=item.audio, type="audio/mpeg"),
                controls="controls",
                preload="metadata"
            )
        return ''

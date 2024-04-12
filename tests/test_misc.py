from clld_audio_plugin import includeme
from clld_audio_plugin.datatables import *
from clld_audio_plugin.maps import ParamMap
from clld_audio_plugin.util import *
from clld_audio_plugin import models


def test_includeme(mocker):
    assert models
    includeme(mocker.MagicMock())


def test_AudioCol(mocker):
    assert AudioCol(mocker.MagicMock(), '').format(mocker.Mock(audio='x'))
    assert not AudioCol(mocker.MagicMock(), '').format(mocker.Mock(audio=None))


def test_form2audio(mocker):
    res = form2audio(mocker.MagicMock(
        iter_rows=lambda *args: [dict(mimetype='audio/mpeg', formReference='x')],
        get_row_url=lambda *args: 'http://example.org'))
    assert res['x'] == 'http://example.org'


def test_ParamMap(mocker):
    assert ParamMap(mocker.Mock(), mocker.Mock()).options['with_audioplayer']

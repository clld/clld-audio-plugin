from clld_audio_plugin import includeme
from clld_audio_plugin.datatables import *
from clld_audio_plugin.maps import ParamMap
from clld_audio_plugin.util import *


def test_includeme(mocker):
    includeme(mocker.MagicMock())


def test_AudioCol():
    pass


def test_form2audio():
    pass

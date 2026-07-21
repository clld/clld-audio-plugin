import pathlib

import pytest

from clld_audio_plugin import includeme
from clld_audio_plugin.datatables import *
from clld_audio_plugin.maps import ParamMap
from clld_audio_plugin.util import *
from clld_audio_plugin import models

from pycldf import Dataset


def test_includeme(mocker):
    assert models
    includeme(mocker.MagicMock())


def test_AudioCol(mocker):
    assert AudioCol(mocker.MagicMock(), '').format(mocker.Mock(audio='x'))
    assert not AudioCol(mocker.MagicMock(), '').format(mocker.Mock(audio=None))


@pytest.mark.parametrize(
    'ds',
    [
        'dataset_with_formReference',
        'dataset_without_mediatable',
        'dataset_with_mediaReference',
        'dataset_with_valueUrl',
    ],
)
def test_form2audio(ds):
    ds = Dataset.from_metadata(pathlib.Path(__file__).parent / ds / 'metadata.json')
    res = form2audio(ds)
    assert 'cdstar.eva' in res['1']


def test_ParamMap(mocker):
    assert ParamMap(mocker.Mock(), mocker.Mock()).options['with_audioplayer']

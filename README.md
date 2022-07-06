# clld-audio-plugin

[![Build Status](https://github.com/clld/clld-audio-plugin/workflows/tests/badge.svg)](https://github.com/clld/clld-audio-plugin/actions?query=workflow%3Atests)
[![codecov](https://codecov.io/gh/clld/clld-audio-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/clld/clld-audio-plugin)
[![PyPI](https://img.shields.io/pypi/v/clld-audio-plugin.svg)](https://pypi.org/project/clld-audio-plugin)

A plugin for the [`clld`](https://pypi.org/project/clld) package.


## Usage

`clld-audio-plugin` provides
- A model class [`clld_audio_plugin.models.Counterpart`](src/clld_audio_plugin/models.py) augmented with an `audio` column to store the URL to an audio file.
- A column for a `DataTable` [`clld_audio_plugin.datatables.AudioCol`](src/clld_audio_plugin/datatables.py) to display objects with an `audio` attribute as audio player.
- A map class [`clld_audio_plugin.maps.ParamMap`](src/clld_audio_plugin/maps.py) specifying a parameter map integrating clld audioplayer functionality.
- Static resources for the configuration/layout of the UI elements contributed by the plugin.

To use map and static resources, include the plugin in your app's `main` function:
```python
    config.include('clld_audio_plugin')
```

To use model and column, just import in your app's `datatables.py` or `models.py` as needed.

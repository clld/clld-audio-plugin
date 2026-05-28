"""
Support for apps that have audio files associated with forms, such as the *Voices series.
"""
from clld_audio_plugin import maps


def includeme(config):  # pylint: disable=C0116
    config.add_static_view('clld-audio-plugin-static', 'clld_audio_plugin:static')
    config.registry.settings['mako.directories'].insert(1, 'clld_audio_plugin:templates')
    maps.includeme(config)

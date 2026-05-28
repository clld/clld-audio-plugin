"""
A ParameterMap class with audioplayer support.
"""
from clld.web.maps import ParameterMap


class ParamMap(ParameterMap):
    """ParameterMap which activates audioplayer support."""
    def get_options(self):  # pylint: disable=C0116
        return {
            'with_audioplayer': True,
            'max_zoom': 13,
            'base_layer': 'OpenTopoMap',
            'show_labels': True,
            'resize_direction': 's',
        }


def includeme(config):  # pylint: disable=C0116
    config.register_map('parameter', ParamMap)

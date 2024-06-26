from clld.web.maps import ParameterMap


class ParamMap(ParameterMap):
    def get_options(self):
        return {
            'with_audioplayer': True,
            'max_zoom': 13,
            'base_layer': 'OpenTopoMap',
            'show_labels': True,
            'resize_direction': 's',
        }


def includeme(config):
    config.register_map('parameter', ParamMap)

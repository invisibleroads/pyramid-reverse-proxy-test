from pyramid.config import Configurator


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.add_route('home', '/')
        config.add_view(my_view, route_name='home', renderer='json')
    return config.make_wsgi_app()


def my_view(request):
    return {'url': request.route_url('home')}

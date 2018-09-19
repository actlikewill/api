from . import api_v1

@api_v1.app_errorhandler(404)
def page_not_found(e):
    return 'Page not found'

@api_v1.app_errorhandler(500)
def server_error(e):
    return 'There was a server error'
    
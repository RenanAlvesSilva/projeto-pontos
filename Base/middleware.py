# middleware.py
class UserGroupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.is_operador = request.user.groups.filter(name='Operador').exists()
            request.is_gerencia = request.user.groups.filter(name='Gerencia').exists()
            request.is_fiscal = request.user.groups.filter(name='Fiscal').exists()
        else:
            request.is_operador = False
            request.is_gerencia = False
            request.is_fiscal = False

        response = self.get_response(request)
        return response

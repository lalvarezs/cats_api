from accounts.models import User


class UserRegisterSerializer:
    def validate_fields(self, request):
        field_list = ['name', 'username', 'cpf', 'email', 'password1', 'password2']
        for field in field_list:
            if not request.data.get(field):
                return {field: ['Esse campo é obrigatório.']}, 400
        return [], 200

    def create_user(self, request):
        try:
            User.objects.create_user(
                name=request.data.get('name'),
                username=request.data.get('username'),
                email=request.data.get('email'),
                cpf=request.data.get('cpf'),
                phone=request.data.get('phone'),
                password=request.data.get('password1'),
            )
            return {'detail': 'Usuário foi criado. com sucesso.'}, 201
        except Exception as e:
            return {'detail': 'Usuário não pode ser criado.'}, 400
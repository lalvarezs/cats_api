from cats.models import Cat

class CatSerializer: 
    def get_all_cats(self, request): 
        cat_list = Cat.objects.filter(user=request.user).values()
        return cat_list, 200

    def validate_fields(self, request):
        field_list = ['name', 'color', 'birthdate']
        for field in field_list:
            if not request.data.get(field):
                return {field: ['Esse campo é obrigatório.']}, 400
        return [], 200

    def create_cat(self, request):
        try:
            Cat.objects.create(
                user=request.user,
                name=request.data.get('name'),
                color=request.data.get('color'),
                birthdate=request.data.get('birthdate')
            )
            return {'detail': 'Gato foi criado. com sucesso.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Gato não pode ser criado.'}, 400
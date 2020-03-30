from setup 	import constants
from peewee 	import *

db = SqliteDatabase(constants.DB_VIAGEM)

class Viagem(Model):

    id 			= AutoField()
    data_inicio		= DateField()
    data_fim 		= DateField()
    classificacao	= IntegerField()
    nota 		= IntegerField()
    user 		= CharField()

    def requestToJson(request, user):
        id 		= request.json.get('id', None)
        data_inicio	= request.json.get('data_inicio', None)
        data_fim 	= request.json.get('data_fim', None)
        classificacao	= request.json.get('classificacao', None)
        nota 		= request.json.get('nota', None)
        current_user 	= user
        data={ "id": id,  "data_inicio": data_inicio,  "data_fim": data_fim,  "classificacao": classificacao,  "nota": nota, "user" : current_user }
        return data

    def modelToJson(viagens):
        data={ "id": viagens.id,  "data_inicio": viagens.data_inicio,  "data_fim": viagens.data_fim,  "classificacao": viagens.classificacao,  "nota": viagens.nota, "user" : viagens.user }
        return data

    class Meta:
        database = db

if __name__ == '__main__':
    try:
        Viagem.create_table()
        print ('Tabela criada!')
    except OperationalError:
        print ('Tabela ja existe!')

<<<<<<< HEAD
## CRUD EM FLK
=======
## CRUD EM FLASK
>>>>>>> ee07e865fb65e0fc32eb3cd629b0beea1b4674e9

Experiência com um crud usando flask e suas ferramentas

- flask 
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Como rodar esse projeto


```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```


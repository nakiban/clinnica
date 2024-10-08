from http import HTTPStatus

from clinica.config.log_config import logger


def test_create_user(client) -> None:
    user = {
        'username': 'carlos',
        'password': '4536645',
        'email': 'eduardo@hotmail.com',
    }

    response = client.post('/api/user', json=user)

    assert response.status_code == HTTPStatus.CREATED

    user = {
        'username': 'carlos',
        'email': 'eduardo@hotmail.com',
    }

    logger.debug(user)

    assert response.json() == user


def test_lista_usuarios(client) -> None:
    response = client.get('/api/users')
    assert response.status_code == HTTPStatus.OK


def test_usuario_existe(client, user) -> None:
    response = client.get(f'/api/user/{user.id}')

    assert response.status_code == HTTPStatus.OK


def test_update_user(client, user) -> None:
    data = {
        'username': 'carlos',
        'password': '4536645',
        'email': 'eduardo@hotmail.com',
    }

    response = client.patch(f'/api/user/{user.id}', json=data)

    assert response.status_code == HTTPStatus.OK


def test_remove_user(client, user) -> None:
    response = client.delete(f'/api/user/{user.id}')

    assert response.status_code == HTTPStatus.ACCEPTED
    assert response.json() == {'message': 'Deletado com sucesso.'}


def test_usuario_nao_existe(client) -> None:
    id = 0
    response = client.get(f'/api/user/{id}')

    assert response.status_code == HTTPStatus.NOT_FOUND

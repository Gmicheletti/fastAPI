from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Metodo Get'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testUserName',
            'email': 'testusername@test.com',
            'password': 'passUser',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'testUserName',
        'email': 'testusername@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testUserName',
                'email': 'testusername@test.com',
                'id': 1,
            }
        ]
    }


def test_read_user_single(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testUserName',
        'email': 'testusername@test.com',
        'id': 1,
    }


def test_read_user_single_not_found(client):
    response = client.get('/users/99999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '',
            'username': 'testUserName2',
            'email': 'testusername@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testUserName2',
        'email': 'testusername@test.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/99999',
        json={
            'password': '',
            'username': 'testUserName2',
            'email': 'testusername@test.com',
            'id': 99999,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

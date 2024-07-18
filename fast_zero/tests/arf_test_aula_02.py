from http import HTTPStatus

from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

from fast_zero.aula_02 import aula_02


def test_root_deve_retornar_ok_e_ola_mundo_em_html():
    client = TestClient(aula_02)

    response = client.get('/', response_class=HTMLResponse)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}

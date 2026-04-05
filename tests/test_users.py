import allure
from faker import Faker
from schemas.user import UserSchema, CreateUserResponse
from src.endpoints import Endpoints

fake = Faker()


@allure.feature("Users")
def test_get_users_list(api_client):
    with allure.step("Запрашиваем список всех пользователей"):
        response = api_client.get(Endpoints.USERS)

    assert response.status_code == 200

    with allure.step("Валидируем каждого пользователя в списке"):
        users = response.json()
        for user_data in users:
            UserSchema(**user_data)


@allure.feature("Users")
@allure.story("Create New User")
def test_create_user(api_client):
    payload = {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    }

    with allure.step("Отправляем POST запрос на создание пользователя"):
        response = api_client.post(Endpoints.USERS, payload)

    assert response.status_code == 201

    with allure.step("Валидируем структуру ответа и наличие ID"):
        data = response.json()
        validated_user = CreateUserResponse(**data)
        assert validated_user.name == payload["name"]


@allure.feature("Users")
@allure.story("Get Non-existent User")
def test_get_user_not_found(api_client):
    with allure.step("Запрашиваем несуществующего пользователя с ID 999"):
        response = api_client.get("/users/999")

    with allure.step("Проверяем, что статус код 404"):
        assert response.status_code == 404
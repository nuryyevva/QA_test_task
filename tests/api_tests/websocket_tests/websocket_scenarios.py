import requests
import random
from testflows.core import *

user_one = {
    "not_registered": False,
    "email": "test2@example.com",
    "username": "User",
    "password": "12345678",
    "token": None,
}
user_two = {  # for checking the fifth scenario
    "not_registered": False,
    "email": "test22@example.com",
    "username": "User2",
    "password": "12345678",
    "token": None,
}


def register(user_data: dict) -> None:
    with Given("the user registration data"):
        registration_data = {
            "email": user_data["email"],
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

    with When("I am registering the user"):
        reg_url = "http://127.0.0.1:8000/registration/"
        reg_response = requests.post(reg_url, json=registration_data)

    with Then("I expect that the user is registered successfully"):
        assert reg_response.status_code == 201


def get_token(user_data: dict) -> None:
    with Given("the user's credentials"):
        user_credentials = {
            "username": user_data["username"],
            "password": user_data["password"],
        }

    with When("I am obtaining the token"):
        token_url = "http://127.0.0.1:8000/token/"
        token_response = requests.post(token_url, json=user_credentials)

    with Then("I expect that the token is obtained successfully"):
        assert token_response.status_code == 200
        user_data["token"] = token_response.json()["token"]


def generate_package() -> dict:
    return {
        "cam_id": random.randint(1, 99),
        "video_color": {
            "brightness": random.randint(0, 100),
            "contrast": random.randint(0, 100),
            "hue": random.randint(0, 100),
            "saturation": random.randint(0, 100),
        },
        "channel_no": random.randint(1, 2),
        "config_no": random.randint(0, 1),
    }


@TestScenario
def authorized_user_can_send_package(self: Test) -> None:
    if user_one["not_registered"]:  # if user is not registered
        register(user_one)

    if user_one["token"] is None:  # if user did not have a token yet
        get_token(user_one)

    with Given("the package data"):
        package_data = generate_package()  # generate a package data

    with When("I am sending the package"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        send_package_response = requests.post(
            package_url, json=package_data, headers=headers
        )

    with Then("I expect that the package is sent successfully"):
        assert send_package_response.status_code == 201


@TestScenario
def unauthorized_user_cannot_send_package(self: Test) -> None:
    with Given("the package data"):
        package_data = generate_package()

    with When("I am sending the package"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        send_package_response = requests.post(package_url, json=package_data)

    with Then("I expect that the package is not sent successfully"):
        assert send_package_response.status_code == 401


@TestScenario
def valid_package_data_is_successfully_saved(self: Test) -> None:
    if user_one["not_registered"]:
        register(user_one)

    if user_one["token"] is None:
        get_token(user_one)

    with Given("the package data"):
        package_data = generate_package()

    with When("I am saving/sending the valid package"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        send_package_response = requests.post(
            package_url, json=package_data, headers=headers
        )

    with Then("I expect that the package is saved/sent successfully"):
        assert send_package_response.status_code == 201


@TestScenario
def invalid_package_data_returns_validation_error(self: Test) -> None:
    if user_one["not_registered"]:
        register(user_one)

    if user_one["token"] is None:
        get_token(user_one)

    with Given("the package data"):
        package_data = generate_package()

    with When("I am saving/sending the invalid package"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        package_data["cam_id"] = 199  # making the cam_id invalid
        send_package_response = requests.post(
            package_url, json=package_data, headers=headers
        )

    with Then("I expect that the package is saved/sent unsuccessfully"):
        assert send_package_response.status_code == 400
        assert send_package_response.json() == {
            "error": {
                "cam_id": ["Ensure this value is less than or equal to 99."]
            }  # validation message we expect
        }

    with When("I am saving/sending the invalid package"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        package_data["cam_id"] = 99  # correct the previous invalid data
        package_data["video_color"]["saturation"] = 150  # make another case
        send_package_response = requests.post(
            package_url, json=package_data, headers=headers
        )

    with Then("I expect that the package is saved/sent unsuccessfully"):
        assert send_package_response.status_code == 400
        assert send_package_response.json() == {
            "saturation": [
                "Ensure this value is less than or equal to 100."
            ]  # expected message
        }


@TestScenario
def authorized_user_can_view_specific_package(self):
    if user_one["not_registered"]:
        register(user_one)

    if user_one["token"] is None:
        get_token(user_one)

    with When("I am obtaining the data about packages"):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        get_package_data_response = requests.get(package_url, headers=headers)

    with Then("I expect that the data is obtained successfully"):
        assert get_package_data_response.status_code == 200

    with When("I am obtaining the data about a specific package"):
        user_one_package_id = str(
            get_package_data_response.json()["results"][0]["id"]
        )  # I get the very first package ID from the obtained data
        package_url = (
            "http://127.0.0.1:8000/api/v1/package/" + user_one_package_id
        )  # write a path to view that exact package
        headers = {"Authorization": "Token " + str(user_one["token"])}
        get_specific_package_data_response = requests.get(package_url, headers=headers)

    with Then("I expect that the data is obtained successfully"):
        assert get_specific_package_data_response.status_code == 200


@TestScenario
def unauthorized_user_cannot_view_others_package(self):
    if user_one["not_registered"]:
        register(user_one)

    if user_one["token"] is None:
        get_token(user_one)

    with When(
        "I am obtaining the package data of user one in order to use it for user two"
    ):
        package_url = "http://127.0.0.1:8000/api/v1/package/"
        headers = {"Authorization": "Token " + str(user_one["token"])}
        get_user_one_package_data_response = requests.get(package_url, headers=headers)

    with Then("I expect that the data is obtained successfully"):
        assert get_user_one_package_data_response.status_code == 200

    user_one_package_id = str(
        get_user_one_package_data_response.json()["results"][0][
            "id"
        ]  # I get the package ID of user one
    )

    if user_two["not_registered"]:
        register(user_two)

    if user_two["token"] is None:
        get_token(user_two)

    with When(
        "I am obtaining the package data of user one with authorization of user two"
    ):
        package_url = (
            "http://127.0.0.1:8000/api/v1/package/" + user_one_package_id
        )  # I try to view the package data of user one authorizing as user two
        headers = {
            "Authorization": "Token " + str(user_two["token"])
        }  # authorization of user two
        get_user_two_package_data_response = requests.get(package_url, headers=headers)

    with Then("I expect that the user two cannot view the data of user one"):
        assert (
            get_user_two_package_data_response.status_code >= 400
        )  # actually the test fails, because user two can see the user one's data


@TestFeature
def websocket_scenarios(self: Test) -> None:
    for scenario in loads(current_module(), Scenario):
        Scenario(run=scenario, flags=TE)

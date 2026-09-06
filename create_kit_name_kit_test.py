import data
import sender_stand_request


def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    response= sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response= sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert kit_body["name"] == response.json()["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos" \
                                         "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def test_1_kit_name_with_1_character():
    current_kit_body = get_kit_body(data.test_1_project_8)
    positive_assert(current_kit_body)

def test_2_kit_name_with_511_characters():
    current_kit_body = get_kit_body(data.test_2_project_8)
    positive_assert(current_kit_body)

def test_3_kit_name_empty():
    current_kit_body = get_kit_body(data.test_3_project_8)
    negative_assert_code_400(current_kit_body)

def test_4_kit_name_with_512_characters():
    current_kit_body = get_kit_body(data.test_4_project_8)
    negative_assert_code_400(current_kit_body)

def test_5_kit_name_with_special_characters():
    current_kit_body = get_kit_body(data.test_5_project_8)
    positive_assert(current_kit_body)

def test_6_kit_name_with_spacing_between_characters():
    current_kit_body = get_kit_body(data.test_6_project_8)
    positive_assert(current_kit_body)

def test_7_kit_name_with_string_number_characters():
    current_kit_body = get_kit_body(data.test_7_project_8)
    positive_assert(current_kit_body)

def test_8_no_name_in_kit_name():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_code_400(current_kit_body)

def test_9_kit_name_with_numbers():
    current_kit_body = get_kit_body(data.test_9_project_8)
    negative_assert_code_400(current_kit_body)

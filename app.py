import requests

def get_member_by_id(member_id, community_id, api_token):
    # Definir la URL con el ID del miembro y el ID de la comunidad
    url = f'https://app.circle.so/api/v1/community_members/{member_id}?community_id={community_id}'
    
    # Definir el encabezado de autorización
    headers = {
        'Authorization': f'Token {api_token}'
    }

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON y devolverla
        return response.json()
    else:
        # En caso de error, devolver el código de estado y el texto de respuesta
        return {'error': response.status_code, 'message': response.text}
    
def send_message_to_member(community_id, user_email, message_body, api_token):
    # Definir la URL
    url = f'https://app.circle.so/api/v1/messages?community_id={community_id}&user_email={user_email}&message_body={message_body}'
    
    # Definir el encabezado de autorización
    headers = {
        'Authorization': f'Token {api_token}'
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON y devolverla
        return response.json()
    else:
        # En caso de error, devolver el código de estado y el texto de respuesta
        return {'error': response.status_code, 'message': response.text}


# ID del miembro, ID de la comunidad y token de autorización
member_id = 25125036
community_id = 1
api_token = 'QGthNSAUNmWcmsYCpwKDxy3J'
message_body = 'Hello and welcome to my Community'
user_email = 'melisa@datarebels.mx'

# Llamar a la función y obtener los datos del miembro
member_data = get_member_by_id(member_id, community_id, api_token)

response = send_message_to_member(member_id, user_email, message_body, api_token)


# Mostrar los datos del miembro
print(member_data)

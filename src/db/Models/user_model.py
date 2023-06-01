user_schema = {
    '$jsonSchema':{
        'title': 'User Object Validation',
        'required': ['email','password','username','role','date_of_birth','first_name','last_name'],
        'properties': {
            'first_name': {
                'bsonType': 'string',
                'pattern': '^[A-Za-z]{3,}$'
            },
            'last_name': {
                'bsonType': 'string',
                'pattern': '^[A-Za-z]{3,}$'
            },
            'username': {
                'bsonType': 'string',
                'description': 'username is required'
            },
            'email': {
                'bsonType': 'string',
                'pattern': "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$",
                'description': 'email is required'
            },
            'password': {
                'bsonType': 'string',
                'description': 'password is required'
            },
            'role': {
                'enum': ['Admin','Normal'],
                'description': 'role is required'
            },
            'date_of_birth':{
                'bsonType': 'date',
                'description': 'date_of_birth is required'
            },
            'image_url':{
                'bsonType': 'string',
                'description': 'image_url is required'
            }
        }
    }
}
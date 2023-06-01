category_schema = {
    '$jsonSchema': {
        'title': 'Object Validation Category',
        'required': ['name_category','description_category'],
        'properties': {
            'name_category': {
                'bsonType': 'string',
                'description': 'name_category required'
            },
            'description_category':{
                'bsonType':'string', 
                'description': 'description_category required'
            }
        }
    }
}
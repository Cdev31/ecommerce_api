product_schema: dict = {
    '$jsonSchema':{
        'title': 'Product Object Validation',
        'required': ['title','stock','price','category','images_products','brand'],
        'properties': {
            'title': {
                'bsonType': 'string',
                'pattern': '^[A-Za-z0-9\s]{2,}$'
            },
            'stock':{
                'bsonType': 'number',
                'minimum': 5
            },
            'price':{
                'bsonType': 'double',
                'minimum': 1
            },
            'category': {
                'bsonType': 'string',
                'enum': ['Cleaning','Electronic','Shoes','Clothes','Others','Personal Care']
            },
            'images_products': {
                'bsonType':'array',
                'minItems': 3,
                'maxItems': 3,
                'items': {
                    'bsonType': 'string'
                }
            },
            'brand':{
                'bsonType': 'string'
            }
        }
    }
}
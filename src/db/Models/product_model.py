product_schema: dict = {
    '$jsonSchema':{
        'title': 'Product Object Validation',
        'required': ['title','stock','price','category','images_products','brand'],
        'properties': {
            'title': {
                'bsonType': 'string'
            },
            'stock':{
                'bsonType': 'number',
                'minimun': 5
            },
            'price':{
                'bsonType': 'double',
                'minimun': 5
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
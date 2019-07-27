def encode_document(data):
    if isinstance(data, list):
        for item in data:
            item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        data['_id'] = str('_id')

    return data


if __name__ == '__main__':
    from bson.objectid import ObjectId

    data = [{
        '_id': ObjectId('5d2df55632be6c6c63aaf06a'),
        'brand': 'Toyota',
        'model': 'Prado Txl',
        'year': 2018,
        'price': 145000000,
        'image': 'https://www.distoyota.com/sites/default/files/2018-09/prado-tres.jpg'}]

    print(encode_document(data))



def success(data, status, message):

    return {
        'success': True,
        'message': message,
        'status': status,
        'data': data,
    }

def serverError(err, status, message):

    return {
        'success': False,
        'status': status,
        'message': message,
        'error': err,
    }
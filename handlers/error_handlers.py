from connexion.lifecycle import ConnexionRequest, ConnexionResponse
import json


def handle_bad_request(request: ConnexionRequest, exception: Exception) -> ConnexionResponse:
    """
    This function handles cases where a required field value is missing during request parsing, 
    such as when accessing request.form['type'] but the field value is not present. 
    """

    response_body = {'error': 'HTTPException', 'message': str(exception)}
    return ConnexionResponse(
        status_code=400,
        mimetype='application/json',
        body=json.dumps(response_body)
    )

def handle_not_found(request: ConnexionRequest, exception: Exception):
    """
    This function will be invoked when bas url or the route is wrong.
    It returns a JSON response with the error status code, title, and detail message.
    """
    response_body = {'error': 'Not Found', 'detail': 'The requested URL was not found on the server.'}
   
    return ConnexionResponse(status_code=404,body=json.dumps(response_body))


def handle_method_not_allowed(request: ConnexionRequest, exception: Exception):
    """
    This function will be invoked when a provided HTTP method is different then expected.
    It returns a JSON response with the error status code, title, and detail message.
    """
    response_body = {'error': 'HTTPException', 'message': str(exception)}
    return ConnexionResponse(
        status_code=405,
        mimetype='application/json',
        body=json.dumps(response_body)
    )

from connexion.exceptions import ProblemException
def handle_generic_exception(exception: Exception, request: ConnexionRequest):
    """
    Custom error handler for arbitrary ServerError 500.
    This function will be invoked when a ServerError occurs.
    It returns a JSON response with the error status code, title, and detail message.
    """
    if isinstance(exception, ProblemException):
        # If it's a ProblemException, return the Problem JSON response
        return jsonify(exception.to_dict()), exception.status
    else:
        response_body = {'error': 'Internal Server Error', 'detail': 'An unexpected error occurred'}
        return ConnexionResponse(
            status_code=500,
            mimetype='application/json',
            body=json.dumps(response_body)
        )

from flask import jsonify
def handle_file_not_found(problem):
    """
    Sometimes, we also use it to handle cases where data is present but in an unexpected format, 
    which may require raising a ProblemException as 
    # ProblemException(status=400, title='Bad Request', detail='Invalid input data')
    """
    return jsonify(problem.to_dict()), problem.status


def handle_problem_exception(request: ConnexionRequest, exception: Exception) -> ConnexionResponse:
    """
    Sometimes, we also use it to handle cases where data is present but in an unexpected format, 
    which may require raising a ProblemException as 
    # ProblemException(status=400, title='Bad Request', detail='Invalid input data')
    """
    response_body = {'error': 'problem_exception', 'detail': 'problem_exception'}
    return ConnexionResponse(
        status_code=400,
        mimetype='application/json',
        body=json.dumps(response_body)
    )
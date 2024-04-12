import connexion
from handlers import handle_file_not_found, handle_bad_request, handle_not_found,handle_method_not_allowed,handle_generic_exception,handle_problem_exception
import logging
from connexion.exceptions import ProblemException




app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yml',swagger_ui=True, base_path='/1.0')

logging.basicConfig(filename='record.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s %(levelname)s %(name)s : %(message)s')




#Add error handler for 400 bad_request
app.add_error_handler(400, handle_bad_request)

#Add error handler for 404 URL was not found
app.add_error_handler(404, handle_not_found)

#Add error handler for 405 method Change
app.add_error_handler(405, handle_method_not_allowed)

# Register error handler for arbitrary exceptions
app.add_error_handler(Exception, handle_generic_exception)

# #Register error handler for ProblemException
#app.add_error_handler(ProblemException, handle_file_not_found)

#app.add_problem_handler(handle_file_not_found)









if __name__ == '__main__':
    app.run(port=5000)
from flask import request, jsonify
from api_server.utils import DynamoDB
from docx import Document
from connexion.exceptions import ProblemException
import logging
logger = logging.getLogger(__name__)

def parse_file():
    logger.info('This is an INFO message')
    logger.debug('This is a DEBUG message')
    logger.warning('This is a WARNING message')
    logger.error('This is an ERROR message')
    logger.critical('This is a CRITICAL message')

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty file'}),400
    # this code for auto 400 file_type = request.form['type'] and we do not provide  type in request
    #file_type = request.form['type']
    file_type = request.form.get('type')
    if not file_type:
        raise FileNotFoundError(status=400, title='Bad Request', detail='Invalid input data') 
        #both are working
    
        #10/0 #generic error
        return jsonify({'error': 'Type parameter is missing'}), 400
    
    # try:
    #     content = extract_and_store_content(file)
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 400
     
    # Store content in DynamoDB
    # try:
    #     dynamodb = DynamoDB()
    #     dynamodb.put_item(content)
    #     return jsonify({'status': 'Data saved successfully'}), 200
    # except Exception as e:
    #     return jsonify({'error': str(e)}), FileNotFoundError
    
def extract_and_store_content(file):
    document = Document(file)
    content = '\n'.join([paragraph.text for paragraph in document.paragraphs])
    return content

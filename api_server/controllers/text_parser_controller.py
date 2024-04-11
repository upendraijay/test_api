from flask import request, jsonify
from api_server.utils import DynamoDB
from docx import Document

def parse_file():
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty file'}), 400

    content = extract_and_store_content(file)

    # Store content in DynamoDB
    try:
        dynamodb = DynamoDB()
        dynamodb.put_item(content)
        return jsonify({'status': 'Data saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def extract_and_store_content(file):
    document = Document(file)
    content = '\n'.join([paragraph.text for paragraph in document.paragraphs])
    return content
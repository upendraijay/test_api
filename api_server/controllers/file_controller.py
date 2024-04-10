from flask import request, jsonify
from api_server.sunscript_parser import compare_files

def upload_files():
    
    file_type = request.form.get('type')
    if not file_type:
        return jsonify({'error': 'Type parameter is missing'}), 400
    
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Files not found'}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'Empty files'}), 400

    content1 = file1.read().decode('utf-8')
    content2 = file2.read().decode('utf-8')

    # Read files and parse based on type
    if file_type == 'sunscript':
          parsed_text=compare_files(content1, content2)
    elif file_type == 'mosiac':
          parsed_text=compare_files(content1, content2)
    else:
          return jsonify({'error': 'Invalid type parameter'}), 400
    
    return jsonify({'parsed_text': parsed_text}), 200

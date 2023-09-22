from flask import Flask, request, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='PDF Upload API', description='A simple API to upload PDFs')

ns = api.namespace('pdf', description='PDF operations')

parser = api.parser()
parser.add_argument('file', location='files', type='file', required=True, help='The PDF file')

@ns.route('/upload')
class PDFUpload(Resource):

    @ns.expect(parser)
    def post(self):
        uploaded_file = request.files['file']
        try:
            # Simply read the file to ensure it's accessible
            file_content = uploaded_file.stream.read()
            # Since we're not using the content, no need to process it further.
            return {"message": "OK"}, 201
        except Exception as e:
            ns.abort(500, f"Error reading the file: {str(e)}")

if __name__ == "__main__":
    app.run(debug=False)

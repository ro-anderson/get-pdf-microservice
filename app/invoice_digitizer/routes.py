from app.invoice_digitizer.invoice_processing import invoiceProcessing
from app.invoice_digitizer.invoice_upload import InvoiceUpload
from werkzeug.datastructures import FileStorage
from flask_restx import Namespace, Resource


api = Namespace('Invoice Digitizer', description='Invoice Digitizer')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

@api.route('/process-invoice')
class invoiceProcessingRoute(Resource):
    @api.doc(params={'invoice_file_path': 'The invoice file path'})

    def get(self):
        return invoiceProcessing().scanning_invoice

@api.route('/upload-invoice')
@api.expect(upload_parser)
class InvoiceUploadRoute(Resource):
    
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['Invoice file']
        #url = do_something_with_file(uploaded_file)
        return InvoiceUpload().upload_invoice()

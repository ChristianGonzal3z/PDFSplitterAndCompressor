from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfReader, PdfWriter
import os
import zipfile

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/split_and_zip', methods=['POST'])
def split_and_zip():
    file = request.files['file']
    reader = PdfReader(file)
    original_filename = os.path.splitext(file.filename)[0]

    for page_number, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)

        output_filename = f'split_{original_filename}_{page_number}.pdf'
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)

    with zipfile.ZipFile(f'{original_filename}_zipped_pdfs.zip', 'w') as zipf:
        for file in os.listdir():
            if file.startswith('split_') and file.endswith('.pdf'):
                zipf.write(file)
                os.remove(file)

    return send_file(f'{original_filename}_zipped_pdfs.zip', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

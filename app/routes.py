import os
from flask import Blueprint, current_app, flash, request, redirect, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
import pdb

bp = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@bp.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@bp.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('main.view_upload', filename=filename))

@bp.route('/view-upload/<filename>', methods=['GET'])
def view_upload(filename):
    return render_template("show_upload.html", filename=filename)

@bp.route('/uploads/<filename>', methods=['GET'])
def uploads(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


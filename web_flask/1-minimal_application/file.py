from flask import request, render_template, redirect, url_for, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 1. Access the uploaded file
        file = request.files['the_file']

        # 2. Validate filename and extension (optional)
        allowed_extensions = ['txt', 'pdf', 'jpg', 'png']
        if file.filename.split('.')[-1].lower() not in allowed_extensions:
            return render_template('error.html', message="Invalid file type")

        # 3. Generate a secure filename
        filename = secure_filename(file.filename)

        # 4. Save the file to a designated location
        file.save(f"./templates/{filename}")

        # 5. Handle success/error messages
        return render_template('success.html', message="File uploaded successfully!")
    else:
        return render_template('hello.html')
    
if __name__=='__main__':
    app.run(debug=True)
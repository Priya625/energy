import csv
from flask import Flask, render_template , url_for , request , redirect
app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html');
@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)

@app.route('/index.html')
def home1():
  return render_template('index.html');

@app.route('/components.html')
def components():
  return render_template('components.html');

def write_to_file(data):
  with open("database.txt" , mode='a') as database:
    email=data["email"]
    subject=data["Subject"]
    message=data["message"]
    file=database.write(f'\n {email} , {subject} , {message}')

def write_to_csv(data):
  with open("database.csv" , mode='a') as database2:
    email=data["email"]
    subject=data["subject"]
    message=data["message"]
    csv_writer = csv.writer(database2 , delimiter = ',', quotechar = ',' , quoting = csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    write_to_csv(data)
    return redirect('/thankyou.html')
  else :
    return 'something went wrong'

if __name__ == '__main__':
  app.run(debug = True)
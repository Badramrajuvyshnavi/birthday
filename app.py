from flask import Flask, render_template, request, redirect

app = Flask(__name__)

birthdays = []  # simple in-memory list

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        if name and date:
            birthdays.append({'name': name, 'date': date})
        return redirect('/')
    return render_template('index.html', birthdays=birthdays)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port="5000")

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        interviewer = request.form['interviewer']
        total = int(request.form['total'])
        men = int(request.form['men'])
        women = int(request.form['women'])
        if total > 0:
            men_percentage = (men / total) * 100
            women_percentage = (women / total) * 100
        return render_template('index.html', date=date, interviewer=interviewer, total=total, men=men, women=women,
                               men_percentage=men_percentage, women_percentage=women_percentage)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

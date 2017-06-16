from flask import Flask, render_template, request
from application import db
# from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo
from templates.models import results
from creds import APPLICATION_SECRET_KEY
from compute import compute

application = Flask(__name__)
application.debug=True
# need to set from location
application.secret_key = APPLICATION_SECRET_KEY

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EnterDBInfo(request.form)
    form2 = RetrieveDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        test_row = [float(form1.dbNotes.data), 0.53, 2, 157, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
            # test_row = [0.38, 0.53, 2, 157, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        chosen_one = results('joe', float(compute(test_row)))
        result = [chosen_one]
        #db.session.add(chosen_one)
        #db.session.commit()
        #result = db.engine.execute("SELECT * FROM results WHERE employee_name = '" + str(form1.dbNotes.data) + "'")
        return render_template('results.html', result=result)
        #db.session.delete(chosen_one)
        #db.session.commit()

        # return an employee from results table when searched
        # result = db.engine.execute("SELECT * FROM results WHERE employee_name = '" + str(form1.dbNotes.data) + "'")
        # return render_template('results.html', results=result, num_return='1')
    # change this
    elif request.method == 'POST':
        result = db.engine.execute("SELECT * FROM results ORDER BY leave_chance DESC")
        return render_template('results.html', result=result)


    return render_template('index.html', form1=form1, form2=form2)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

from flask import Flask, render_template, request, jsonify
from application import db
# from application.models import Data
from application.forms import EmployeeInfo
from templates.models import results
from creds import APPLICATION_SECRET_KEY
from compute import compute

application = Flask(__name__)
application.debug=True
# need to set from location
application.secret_key = APPLICATION_SECRET_KEY

@application.route('/prediction_app/api/v1.0/pred', methods=['POST'])
def get_prediction():
    var1 = request.json['employee_satisfaction_level']
    var2 = request.json['last_evaluation_score']
    var3 = request.json['number_projects_performed']
    var4 = request.json['average_monthly_hours_worked']
    var5 = request.json['tenure_years']
    var6 = request.json['work_accident']
    if "n" in var6:
        var6 = 0
    else:
        var6 = 1
    var7 = request.json['promotion_in_last_5years']
    if "n" in var7:
        var7 = 0
    else:
        var7 = 1
    input_row = [var1, var2, var3, var4, var5, var6, var7, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    result = str(compute(input_row))
    return result

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EmployeeInfo(request.form)

    if request.method == 'POST' and form1.validate():
        form1.employee_name.data
        form1.s_level.data
        form1.eval_score.data
        form1.number_projects_performed.data
        form1.average_monthly_hours_worked.data
        form1.tenure.data
        wa = 0
        if form1.work_accident.data:
            wa = 1
        p5 = 0
        if form1.promotion_in_last_5years.data:
            p5 = 1
        test_row = [float(form1.s_level.data), float(form1.eval_score.data), form1.number_projects_performed.data, form1.average_monthly_hours_worked.data, form1.tenure.data, wa, p5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
            # test_row = [0.38, 0.53, 2, 157, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        chosen_one = results(form1.employee_name.data, float(compute(test_row)))
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
    # elif request.method == 'POST':
    #     result = db.engine.execute("SELECT * FROM results ORDER BY leave_chance DESC")
    #     return render_template('results.html', result=result)


    return render_template('index.html', form1=form1)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

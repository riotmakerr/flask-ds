from flask import Flask, render_template, request
from application import db
# from application.models import Data
from application.forms import EmployeeInfo
from creds import APPLICATION_SECRET_KEY

application = Flask(__name__)
application.debug=True
# need to set from location
application.secret_key = APPLICATION_SECRET_KEY

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
        form1.work_accident.data
        form1.promotion_in_last_5years.data
        return render_template('results.html', results=result, num_return='1')

        data_entered = Data(notes=form1.dbNotes.results)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.results)

    # elif request.method == 'POST':
        # try:
        #     num_return = int(form2.numRetrieve.Data)
        #     query_db = Data.query.order_by(Data.id.desc()).limit(num_return)
        #     for q in query_db:
        #         print(q.employee_name)
        #     db.session.close()
        # except:
        #     db.session.rollback()
        # result = db.engine.execute("SELECT * FROM results ORDER BY leave_chance DESC")
        # return render_template('results.html', results=result, num_return='1')


    return render_template('index.html', form1=form1)

if __name__ == '__main__':
    application.run(host='0.0.0.0')

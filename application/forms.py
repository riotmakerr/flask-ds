from flask.ext.wtf import Form
from wtforms import TextField, validators, IntegerField, BooleanField, DecimalField, SelectField
from wtforms.fields.html5 import DecimalRangeField

class EmployeeInfo(Form):
    employee_name = TextField(label='Employee Name',  validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
    s_level = DecimalRangeField(label='Satisfaction Level', default = 0, places=2)
    eval_score = DecimalRangeField(label='Evaluation Score', default = 0, places=2)
    number_projects_performed = IntegerField(label='Number of Projects Performed', default = 1)
    average_monthly_hours_worked = IntegerField(label='Average Monthly Hours Worked', default = 160)
    tenure = DecimalField(label='Tenure', default=.01)
    work_accident = BooleanField(label='Work Accident?')
    promotion_in_last_5years = BooleanField(label='Promotion in Last 5 Years')
    salary = SelectField(label='Salary', choices=[('low','Low'),('medium','Medium'),('high','High')])
    department = SelectField(label='Department', choices=[('dep_IT', 'IT'),('dep_accounting', 'Accounting'),('dep_hr', 'HR'), ('dep_management', 'Management'), ('dep_marketing', 'Marketing'),('dep_product_mng', 'Product Management'),('dep_sales', 'Sales'),('dep_support', 'General Support'),('dep_technical', 'Tech Support'),('dep_RandD', 'Other')])

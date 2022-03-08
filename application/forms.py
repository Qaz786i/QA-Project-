from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField


class AddEmployee(FlaskForm):
    first_name = StringField("Employee's First Name")
    last_name = StringField("Employee's Last Name")
    email = StringField("Employee's email address")
    address = StringField("Employee's home address")
    submit = SubmitField("Add Employee")

class AddJob(FlaskForm):
    name = StringField("Job Title")
    details = StringField("Job Description")
    submit = SubmitField("Add Job")

class AddEmployment(FlaskForm):
    fk_employee = SelectField("Employee", choices =[])
    fk_job = SelectField("Job", choices =[])
    submit = SubmitField("Employ this Employee to this Job")

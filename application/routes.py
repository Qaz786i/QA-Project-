from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Employee, Job, Employment
from application.forms import AddEmployee, AddJob, AddEmployment


@app.route('/')
def home():
    num_employees = Employee.query.count()
    employees = Employee.query.all()
    num_job = Job.query.count()
    jobs = Job.query.all()
    employed = Employment.query.all()
    return render_template('index.html', num = num_employees, employees = employees, num_job = num_job, jobs = jobs, employed = employed)

@app.route('/create-employee', methods = ['GET', 'POST'])
def create_employ():
    form = AddEmployee()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address = form.address.data
        new_employee = Employee(first_name = first_name, last_name = last_name, email = email, address = address)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_employee.html', form = form, ptitle = "Add Employee")

@app.route('/create-job', methods = ['GET', 'POST'])
def create_job():
    form = AddJob()
    if request.method == 'POST':
        name = form.name.data
        details = form.details.data
        new_job = Job(name = name, details = details)
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_job.html', form =form)
  

@app.route('/create-employment', methods = ['GET', 'POST'])
def create_employment():
    employee = Employee.query.all()
    job = Job.query.all()
    form = AddEmployment()
    form.fk_employee.choices.extend([( employee.pk, employee.first_name + " " + employee.last_name) for employee in employee])
    form.fk_job.choices.extend([( job.pk, job.name ) for job in job])
    if request.method == 'POST' :
        fk_employee = form.fk_employee.data
        fk_job = form.fk_job.data
        new_employment = Employment(fk_employee = fk_employee, fk_job = fk_job)
        db.session.add(new_employment)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_employment.html', form = form, ptitle = "Create Employment")

@app.route('/update-employement/<int:pk>', methods = ['GET', 'POST'])
def update_employment(pk):
    employment = Employment.query.get(pk)
    employee = Employee.query.all()
    job = Job.query.all()
    form = AddEmployment()
    form.fk_employee.choices.extend([( employee.pk, employee.first_name + " " + employee.last_name) for employee in employee])
    form.fk_job.choices.extend([( job.pk, job.name ) for job in job])
    if request.method == 'POST' :
        employment.fk_employee = int(form.fk_employee.data)
        employment.fk_job = int(form.fk_job.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_employment.html', form = form, ptitle = "Update Employment") 

@app.route('/delete-employement/<int:pk>', methods = ['GET', 'POST'])
def delete_employment(pk):
    employment = Employment.query.get(pk)
    db.session.delete(employment)
    db.session.commit()
    return redirect(url_for('home'))        

@app.route('/update-employee/<int:pk>', methods = ['GET', 'POST'])    
def update_employee(pk):
    employee = Employee.query.get(pk)
    form = AddEmployee()
    if request.method == 'POST' :
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        employee.email = form.email.data
        employee.address = form.email.data 
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_employee.html', form = form, ptitle = "Update Employee")

@app.route('/delete-employee/<int:pk>', methods = ['GET', 'POST'])
def delete_employee(pk):
    employee = Employee.query.get(pk)
    employments = Employment.query.filter_by(fk_employee = employee.pk).all()
    for employment in employments:
        db.session.delete(employment)
        db.session.commit()    
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('home'))
    
@app.route('/update-job/<int:pk>', methods = ['GET', 'POST'])
def update_job(pk):
    job = Job.query.get(pk)
    form = AddJob()
    if request.method == 'POST' :
        job.name = form.name.data
        job.details = form.details.data 
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_job.html', form = form, ptitle = "Update Job")
    
@app.route('/delete-job/<int:pk>', methods = ['GET', 'POST'])
def delete_job(pk):
    job = Job.query.get(pk)
    employments = Employment.query.filter_by(fk_job = job.pk).all()
    for employment in employments:
        db.session.delete(employment)
        db.session.commit()
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('home'))        
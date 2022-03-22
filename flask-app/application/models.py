from application import db 

class Employee(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    address = db.Column(db.String(50))
    employee_employ = db.relationship('Employment', backref = 'employee')
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} Address: {self.address} Email: {self.email}"


class Job(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    details = db.Column(db.String(50))
    job_employment = db.relationship('Employment', backref = 'job')
    def __str__(self):
        return f"{self.name}: {self.details}"


class Employment(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    fk_employee = db.Column(db.Integer, db.ForeignKey("employee.pk"))
    fk_job = db.Column(db.Integer, db.ForeignKey("job.pk"))
    def __str__(self):
        return f"{Employee.query.get(self.fk_employee).first_name} has been employed for the role : {Job.query.get(self.fk_job).name}"
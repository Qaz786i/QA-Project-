from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Employee, Job, Employment

class TestBase(TestCase):
    def create_app(self):   # Sets test configuation
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "test_secret_key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app 

    def setUp(self): #Run before each test
        db.create_all()
        sample_employee = Employee(first_name = "Bruce", last_name = "Wayne", email = "bwayne@gotham.co.uk", address = "1 Gotham Road")
        sample_job = Job(name = "CEO", details = "CEO of Wayne Enterprise")
        sample_employment = Employment(fk_employee = 1, fk_job = 1)

        db.session.add(sample_employee)
        db.session.add(sample_job)
        db.session.add(sample_employment)
        db.session.commit()

    def tearDown(self):  #Run after each test
        db.session.remove()
        db.drop_all()


class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'CEO', response.data)


class Test_create_employ(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_employ'))
        self.assert200(response)
        self.assertIn(b'Employees First Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('create_employ'),
            data = dict(first_name = "Ikora", last_name = "Ray", email = "destiny@343.com", address = "1 Yes Road"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Ikora', response.data)

class Test_create_job(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_job'))
        self.assert200(response)
        self.assertIn(b'Job Title', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('create_job'),
            data = dict(name = "Manager", details = "Manage operations"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Manager', response.data)

class Test_create_employment(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_employment'))
        self.assert200(response)
        self.assertIn(b'Employee', response.data)
    
    def test_create_post(self):
        response = self.client.post(
            url_for('create_employment'),
            data = dict(fk_employee = 1, fk_job = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'1', response.data)


class Test_update_employee(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('update_employee', pk=1))
        self.assert200(response)
         

    def test_create_post(self):
        response = self.client.post(
            url_for('update_employee', pk=1),
            data = dict(first_name = "John", last_name = "Wick", email = "jwick'yes.com", address = "1 Wick Way"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'John', response.data)

class Test_update_job(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('update_job', pk=2))
        self.assert200(response)
        self.assertIn(b'Job Title', response.data) 

    def test_create_post(self):
        response = self.client.post(
            url_for('update_job', pk=2),
            data = dict(name = "Manager", details ="QA"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Manager', response.data)


class Test_update_employment(TestBase):    
    def test_create_get(self):
        response = self.client.get(url_for('update_employment', pk=1))
        self.assert200(response)
        self.assertIn(b'Employee', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('update_employment', pk=3),
            data = dict(fk_employee = 2, fk_job = 2),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'has been employed for the role', response.data)

class Test_delete_employee(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('delete_employee', pk=1), follow_redirects = True )
        self.assert200(response)
        self.assertNotIn(b'Address', response.data)


class Test_delete_job(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('delete_job', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'CEO', response.data)


class Test_delete_employment(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('delete_employment', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'has been employed for the role', response.data)                

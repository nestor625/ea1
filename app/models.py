import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

# Flask-AppBuilder 5 no longer derives table names from class names.
# These names match the ones version 1.12 generated.

class Gender(Model):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    __tablename__ = 'function'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    __tablename__ = 'benefit'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    __tablename__ = 'employee_history'
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
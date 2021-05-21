from flask_script import Manager, prompt_bool, Command
from app import db

manager = Manager(usage="Perform database operations")

@manager.command
def drop():
    """Drops database tables"""
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()

@manager.command
def createdb():
    """Delete database """
    if prompt_bool("Do you create a database?"):
        db.create_all()

@manager.command
def recreate():
    """Rebuild the database """
    if prompt_bool("Do you want to rebuild the database?"):
        drop()
        createdb()

@manager.command
def init_data():
    pass    
    print("initialization completed")
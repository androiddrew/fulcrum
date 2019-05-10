from flask_script import Manager, prompt_bool
from sqlalchemy.exc import IntegrityError
from fulcrum import create_app, db
from fulcrum.models import Role, ToDo, User, Address, Email

app = create_app("dev")
manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    print("Database Initialized")


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop the database?"):
        if prompt_bool(
            "You could really mess things up, are you sure you want to drop the db?"
        ):
            db.drop_all()
            print("Database tables dropped")
        else:
            print("Ok we are not going to drop the db today")


@manager.command
def test_data():
    """Populate initial data in the test db"""
    try:
        user = User(first_name="Android", last_name="Drew", is_confirmed=True)
        admin = Role(name="ADMIN")
        address = Address(
            address_line1="1234 Fake St.",
            city="Sin City",
            state="MI",
            zip="12345",
            country="US",
        )
        email = Email(email="fake@gmail.com")
        user.roles.append(admin)
        user.mail_addresses.append(address)
        user.email_addresses.append(email)
        new_todo = ToDo(title="MILK", task="don't forget the milk")
        user.to_dos.append(new_todo)
        db.session.add(user)
        db.session.commit()
        print("Test data created")
    except IntegrityError as e:
        db.session.rollback()
        print("Transaction rolledback due to Integrity Error\n", str(e))


if __name__ == "__main__":
    manager.run()

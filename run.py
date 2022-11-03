# message flashing for form erros not working as expected
from flaskblog import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

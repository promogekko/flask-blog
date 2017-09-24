from models import User, db

user = User.create("charlie@gmail.com", password="secret", name="Charlie")

db.session.add(user)
db.session.commit()


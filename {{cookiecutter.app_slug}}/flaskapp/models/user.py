from flaskapp.extensions import db
from fuser.user_mixin import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


class User(db.Model, UserMixin):
    # __tablename__ = 'user'
    name = db.Column(db.Text(), nullable=False, unique=True)

	# Example relationships    
    # group_id = db.Column(db.Integer, ForeignKey('category_group.id'), nullable=False)
    # transactions = db.relationship("Transaction", backref="category")

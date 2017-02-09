from flaskapp.extensions import db
from pga.basemodel import BaseModelMixin
from sqlalchemy import ForeignKey


class Category(db.Model, BaseModelMixin):
    name = db.Column(db.Text(), nullable=False, unique=True)

	# Example relationships    
    # group_id = db.Column(db.Integer, ForeignKey('category_group.id'), nullable=False)
    # transactions = db.relationship("Transaction", backref="category")

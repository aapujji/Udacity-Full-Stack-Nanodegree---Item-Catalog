import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    brand = Column(String(80), nullable=False)
    description = Column(String(250))
    image = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'description': self.description,
            'image': self.image
        }


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)

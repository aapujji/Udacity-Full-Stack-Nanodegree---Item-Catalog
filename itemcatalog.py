from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(Category=[c.serialize for c in categories])


@app.route('/categories/<int:category_id>/items/JSON')
def categoryItemsJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/categories/<int:category_id>/items/<int:item_id>/JSON')
def itemJSON(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)


@app.route('/')
@app.route('/categories')
def viewCategories():
    #return "Page to view categories"
    categories = session.query(Category).all()
    items = session.query(Item).order_by(Item.id.desc())
    return render_template('categories.html',categories = categories,items=items)


@app.route('/categories/add', methods=['GET','POST'])
def addCategory():
    if request.method == 'POST':
        newCategory = Category(name = request.form['name'], image = request.form['image'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('viewCategories'))
    else:
        return render_template('add-category.html')


@app.route('/categories/<int:category_id>/edit', methods=['GET','POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
        if request.form['image']:
            editedCategory.image = request.form['image']
        session.add(editedCategory)
        session.commit()
        return redirect(url_for('viewCategories'))
    else:
        return render_template('edit-category.html', category=editedCategory)

@app.route('/categories/<int:category_id>/delete', methods=['GET','POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('viewCategories', category_id=category_id))
    else:
        return render_template('delete-category.html', category=categoryToDelete)


@app.route('/categories/<int:category_id>')
@app.route('/categories/<int:category_id>/items')
def viewItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id).all()
    return render_template('category-items.html', category=category, items=items, category_id=category.id)


@app.route('/categories/<int:category_id>/items/<int:item_id>')
def viewItem(category_id, item_id):
    clickedItem = session.query(Item).filter_by(id=item_id).one()
    return render_template('item.html', category_id = category_id, item_id = item_id, item = clickedItem)


@app.route('/categories/<int:category_id>/add', methods=['GET','POST'])
def addItem(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Item(name = request.form['name'], brand = request.form['brand'], description = request.form['description'], image = request.form['image'], category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('viewItems', category_id=category_id))
    else:
        return render_template('add-item.html', category_id = category_id)


@app.route('/categories/<int:category_id>/items/<int:item_id>/edit', methods=['GET','POST'])
def editItem(category_id, item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['brand']:
            editedItem.brand = request.form['brand']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['image']:
            editedItem.image = request.form['image']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('viewItem', category_id = category_id, item_id = item_id, item=editedItem))
    else:
        return render_template('edit-item.html', category_id = category_id, item_id = item_id, item=editedItem)


@app.route('/categories/<int:category_id>/items/<int:item_id>/delete', methods = ['GET','POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('viewItems',category_id=category_id))
    else:
        return render_template('delete-item.html',item=itemToDelete)     
    

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

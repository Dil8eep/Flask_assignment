from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class ItemForm(FlaskForm):
    new_item = StringField('New Item', [validators.DataRequired()])
    submit = SubmitField('Add Item')

@app.route('/')
def index():
    items = Item.query.all()
    form = ItemForm()
    return render_template('index.html', items=items, form=form)

@app.route('/add', methods=['POST'])
def add_item():
    form = ItemForm()

    if form.validate_on_submit():
        new_item = form.new_item.data
        item = Item(name=new_item)
        db.session.add(item)
        db.session.commit()
        flash(f'Item "{new_item}" added successfully!', 'success')
    else:
        flash('Invalid input. Item not added.', 'danger')

    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)

    if item:
        db.session.delete(item)
        db.session.commit()
        flash(f'Item "{item.name}" deleted successfully!', 'success')
    else:
        flash('Item not found. Deletion failed.', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

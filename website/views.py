from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Reporte
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/Reports', methods=['GET', 'POST'])
@login_required
def reports():
    if request.method == 'POST':
        note = request.form.get('reporte')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("reports.html", user=current_user)

@views.route('/delete-reporte', methods=['POST'])
def delete_reporte():
    reporte = json.loads(request.data)
    reporteId = reporte['reporteId']
    reporte = Reporte.query.get(reporteId)
    if reporte:
        if reporte.user_id == current_user.id:
            db.session.delete(reporte)
            db.session.commit()

    return jsonify({})

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/Report', methods=['GET', 'POST'])
@login_required
def report():
    #if request.method == 'POST':
        #note = request.form.get('note')

        #if len(note) < 1:
            #flash('Note is too short!', category='error')
        #else:
            #new_note = Note(data=note, user_id=current_user.id)
            #db.session.add(new_note)
            #db.session.commit()
            #flash('Note added!', category='success')

    return render_template("reporteDet.html", user=current_user)

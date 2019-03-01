import sys
from flask import Flask, Blueprint, redirect, current_app, request, session, g, abort, render_template, Response
from flask_login import login_required, current_user

from models.user import *

access_control = Blueprint('access_control', __name__)

#showcase the item list to verify
@access_control.route('/user_list', methods=['GET'])
@login_required
def user_list():
  try:
    if request.method == 'GET':
      users = fetch_users()
      return render_template("access_control/user_list.html",users=users)
  except Exception as e:
    print e
    return render_template("access_control/user_list.html")


@access_control.route('/change_role/<uid>', methods=['GET'])
@login_required
def change_role(uid):
  try:
    if request.method == 'GET':
      change_user_role(uid)
      return redirect("/user_list")
  except Exception as e:
    return redirect("/user_list")

@access_control.route('/delete_user/<uid>', methods=['GET'])
@login_required
def delete_user(uid):
  try:
    if request.method == 'GET':
      delete_user_data(uid)
      return redirect("/user_list")
  except Exception as e:
    return redirect("/user_list")


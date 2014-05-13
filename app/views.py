# This is the file that contains all the route handlers.
from app import app, queue_server
import database_utilities as db_util
import sqlite3
from flask import request, session, g, redirect, url_for, abort, jsonify
import permissions

from q_classes import QueueServer, QueueMember, QueueSettings

# This procedure picks up the default route and returns index.html.
@app.route('/')
def root():
   return app.send_static_file('index.html')

@app.route('/join', methods=['POST'])
def add_to_queue():
   """Joins a queue defined by the 'qid' passed as a parameter.

   If the session is not logged in, assumes that the user is a temporary user,
   and looks for a 'uname' parameter as well. This will create a temporary
   user.

   Returns: example return value below
      {
         "avg_wait_time": null,
         "confirmation_number": 1472823387,
         "expected_wait": null,
         "member_position": 0,
         "name": "ohhey",
         "q_ID": 556035656,
         "size": 1
      }
   """
   
   uid = None
   username = None
   qid = int(request.json['qid'])
   temp = None
   if session.has_key('logged_in') and session['logged_in']:
      uid = session['uid']
      username = session['uname']
   else:
      temp = True
      temp_user = dict()
      temp_user['uname'] = request.json['uname']
      try:
         temp_user['id'] = db_util.create_temp_user(temp_user)
      except sqlite3.Error as e:
         return e.message
      username = temp_user['uname']
      uid = temp_user['id']
   if not permissions.has_flag(uid, qid, permissions.BLOCKED_USER):
      q_member = QueueMember(username, uid)
      queue_server.add(q_member, qid)
      q_info = queue_server.get_info(q_member, qid)
      q_info_dict = dict(q_info.__dict__)
      if temp:
         q_info_dict['confirmation_number'] = uid
      return jsonify(q_info_dict)
   else:
      return 'User is blocked from this queue.'

@app.route('/login', methods=['GET','POST'])
def login():
   return 'Not implemented yet!'

@app.route('/dequeue', methods=['POST'])
def dequeue():
   return 'Not implemented yet!'

@app.route('/searchResults')
def get_search_results():
   return 'Not implemented yet!'

@app.route('/search')
def search():
   return 'Not implemented yet!'

@app.route('/memberQueue', methods=['POST'])
def get_member_queue():
   return 'Not implemented yet!'

@app.route('/employeeQueue/<qid>')
def get_employee_queue(qid):
   return 'Not implemented yet!'

@app.route('/adminQueue/<qid>')
def get_admin_queue(qid):
	return

@app.route('/queueStatus/<qid>')
def get_queue_status():
   """View the queue with the given qid.

   Returns: example return value below
      {
         "avg_wait_time": null,
         "confirmation_number": 1472823387,
         "expected_wait": null,
         "member_position": 0,
         "name": "ohhey",
         "q_ID": 556035656,
         "size": 1
      }
   """
   q_info = queue_server.get_info(None, qid)
   return jsonify(q_info.__dict__)

@app.route('/myQueues')
def get_my_queues():
	return 'Not implemented yet!'

@app.route('/remove')
def remove_queue_member():
	return 'Not implemented yet!'

@app.route('/qtracks')
def queue_tracks():
	return 'Not implemented yet!'

@app.route('/qtracksData')
def queue_tracks_data():
	return 'Not implemented yet!'

@app.route('/createUser', methods=['POST'])
def create_user():
   user_data = request.json
   try:
      user_data['id'] = db_util.create_user(user_data)
      return jsonify(user_data)
   except sqlite3.Error as e:
      return e.message

@app.route('/createQueue', methods=['POST'])
def create_queue():
   # q_settings = request.form.copy()
   q_settings = request.json
   try:
      q_settings['id'] = db_util.create_queue(q_settings)
      return jsonify(q_settings)
   except sqlite3.Error as e:
      return e.message

@app.route('/logout')
def logout():
	return 'Not implemented yet!'

""" Database models for the CMS user """

from flask_mongoengine import MongoEngine
from ..base import BaseDocument
from bson.objectid import ObjectId

db = MongoEngine()

class CmsUser(BaseDocument):
    """ A CmsUser model defining some fields

    :param email email: Email or username of CMS User
    :param string mobile: Mobile number 
    :param string password: Encrypted password
    :param string fullname: Full name of user
    :param string auth_token: Authorization Token required each time user make call to services
    :param datetime last_logged_in: Last Login time of user
    :param reference userrole: Role of user selected from all roles
    :param reference userlog: List of sessions when user logged in
    :param reference action_type: List of user action_type

    """
    email = db.EmailField(unique=True,required=True)
    mobile = db.StringField()
    password = db.StringField(required=True) 
    full_name = db.StringField() # Should be required
    action_type = db.StringField() #ADMIN HAVE RWD #USER HAVE R
    auth_token = db.StringField()
    last_logged_in = db.DateTimeField()
    userrole = db.ReferenceField('CmsUserRole')
    userlog = db.ListField(db.ReferenceField('CmsUserLog'))
    block = db.BooleanField(default=False)
    status = db.BooleanField(default=False)
    meta = {'indexes':['email','auth_token']}

    def to_json1(self):
        """Return CmsUser class data in JSON format"""
        return {"id":str(self.id),"email":self.email,"mobile":self.mobile,"name":self.first_name}

class CmsUserLog(BaseDocument):
    """A CmsUserLog class defining some fields
    
    :param reference user: Admin panel user reference
    :param datetime login_time: Date and time of user login to the admin panel
    :param list_of_string user_activity: user activity during the session
    :param datetime logout_time: Date and time of user logged out of the admin panel
   
    """
    user = db.ReferenceField('CmsUser')
    login_time = db.DateTimeField()
    user_activity = db.ListField(db.StringField())
    logout_time = db.DateTimeField()

class CmsUserRole(BaseDocument):
    """A CmsUserRole class defining some fields
    
    :param string name: Name of Role
    :param string desc: Description of Role
    :param list_of_string allowed: Allowed Permissions to the user
   
    """
    name = db.StringField(required=True)
    desc = db.StringField()
    allowed = db.ListField(db.StringField())

def fetch_users():
    roles = CmsUserRole.objects(name__in=['assistant','user']).all()
    users = CmsUser.objects(userrole__in=roles).all()
    if users:
        return users
    else:
        return []

def change_user_role(uid):
    user = CmsUser.objects(id=ObjectId(uid)).first()
    role = user.userrole.name
    if role == "user":
        assign_role = CmsUserRole.objects(name="assistant").first()
        user.userrole = assign_role
        user.action_type = "RW"
        user.save()
    else:
        assign_role = CmsUserRole.objects(name="user").first()
        user.userrole = assign_role
        user.action_type = "R"
        user.save()

def delete_user_data(uid):
    user = CmsUser.objects(id=ObjectId(uid)).first()
    user.delete()

from sqladmin import ModelView
from mysite.database.models import UserProfile

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [
        UserProfile.id,
        UserProfile.username,
        UserProfile.first_name,
        UserProfile.last_name,
        UserProfile.phone_number,
        UserProfile.password]

# Note: permissions is configured in views.py

from rest_framework import permissions

# BasePermission: for making yur custom permission class 
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    # once request is made 
    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        
        # SAFE_METHODS: don't make any changes to the object, just viewing it
        # if the method is HTTP GET, then it will allow the request
        if request.method in permissions.SAFE_METHODS:
            return True

        # if a user is trying HTTP PUT to upate a profile
        # check if their authenification id matches
        # returns either TRUE or FALSE
        return obj.id == request.user.id
    
### CREATING A PROFILE FEED API ###


# Add a new permissions class that's very similar to the UpdateOwnProfile class
# but it's for updating the users own status.
# Ensure that if a user is updating a status that it's a status that's assigned
# to their user account. This way users can only update their own feed items in the
# database.

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""

        # if a user is trying to retrieve or create their own item, ruturn True
        if request.method in permissions.SAFE_METHODS:
            return True
        # if a user is using HTTP method other than GET, check if that requested object's id is the same as user's id 
        return obj.user_profile.id == request.user.id

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
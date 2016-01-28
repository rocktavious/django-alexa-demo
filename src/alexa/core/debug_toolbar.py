

def show_toolbar(request):
    """
    determine whether to show the toolbar on a given page.
    """
    if request.user.is_anonymous() is False:
        if request.user.alexauser.debug_toolbar:
            return True
    return False

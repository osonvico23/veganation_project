from veganation.models import UserForm

class LoginFormMiddleware(object):

    def process_request(self, request):

        # if the top login form has been posted
        if request.method == 'POST' and 'is_top_login_form' in request.POST:

            # validate the form
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():

                # log the user in
                from django.contrib.auth import login
                login(request, form.get_user())

                # if this is the logout page, then redirect to /
                # so we don't get logged out just after logging in
                if '/account/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')

        else:
            form = AuthenticationForm(request)

        # attach the form to the request so it can be accessed within the templates
        request.login_form = form

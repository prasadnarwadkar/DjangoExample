import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import uuid

from heroes.models import Avenger
from heroes.services import HeroService, HeroServiceInvokeExtApi, HeroServiceSqlite
from heroes.forms import LoginForm, NameForm, NewNameForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

# For using external API, you will need to deploy the API on your environment.
# For quickstart, please use Sqlite3 DB.
service: HeroService = HeroServiceSqlite()


def catch_all(request, unmatched):
    return HttpResponse(f"Unmatched URL: {unmatched}")


@login_required
def heroes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    logger.debug("heroes:")

    avengers = service.getall(request)

    return render(request, "main_app/home.html", {"avengers": avengers})


@login_required
def details(request, id):

    logger.debug("details:" + str(id))

    if request.method == "POST":
        form = NameForm(request.POST)

        if form.is_valid():
            name = form.data["avenger_name"]
            id = form.data["avenger_id"]

            result = service.update_avenger(request, Avenger(name=name, id=id))

            if result:
                return HttpResponseRedirect("/heroes/")
            else:
                print("Save failed.")
        else:
            return render(request, "main_app/error.html", {"errors": form.errors})
    else:
        avenger = service.getbyid(request, id)

        if len(avenger) == 0:
            form = NameForm(
                data={
                    "avenger_name": "",
                    "avenger_id": "",
                    "error": "Not found",
                    "disable_save": "disabled",
                    "hint_text": "Data With the Given ID Has Not Been Found and Cannot Be Saved Back to the Database.",
                }
            )
            return render(
                request, "main_app/name.html", {"myavenger": None, "form": form}
            )
        else:

            form = NameForm(
                data={
                    "avenger_name": avenger[0].name,
                    "avenger_id": avenger[0].id,
                    "disable_save": "null",
                }
            )
            return render(
                request,
                "main_app/name.html",
                {"myavenger": avenger[0], "form": form},
            )


def loginView(request):
    logger.debug("login:" + str(id))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/heroes/")
        else:
            return render(
                request,
                "main_app/error.html",
                {
                    "errors": {
                        "loginError": "Login Was unsuccessful. Either username or password or both are invalid."
                    }
                },
            )
    else:
        form = LoginForm()
        return render(request, "main_app/login.html", {"form": form})


@login_required
def logoutView(request):
    logout(request)
    return render(request, "main_app/logoutsuccess.html")


@login_required
def delete(request, id):
    if request.method == "POST":
        form = NewNameForm(request.POST)

        if form.is_valid():
            try:
                result = service.delete_avenger(request, form.data["avenger_id"])

                if result:
                    return HttpResponseRedirect("/heroes/")
                else:
                    print("Save failed.")
            except Exception as e:
                form = NameForm(
                    data={
                        "avenger_name": form.data["avenger_name"],
                        "avenger_id": form.data["avenger_id"],
                        "error": e.args,
                        "disable_save": "disabled",
                        "hint_text": "There was an error while deleting the avenger from the database.",
                    }
                )
            return render(
                request, "main_app/delete.html", {"myavenger": None, "form": form}
            )
    else:
        avenger = service.getbyid(request, id)

        if len(avenger) == 0:
            form = NameForm(
                data={
                    "avenger_name": "",
                    "avenger_id": "",
                    "error": "Not found",
                    "disable_save": "disabled",
                    "hint_text": "Data With the Given ID Has Not Been Found and Cannot Be Saved Back to the Database.",
                }
            )
            return render(
                request, "main_app/delete.html", {"myavenger": None, "form": form}
            )
        else:

            form = NameForm(
                data={
                    "avenger_name": avenger[0].name,
                    "avenger_id": avenger[0].id,
                    "disable_save": "null",
                }
            )
            return render(
                request,
                "main_app/delete.html",
                {"myavenger": avenger[0], "form": form},
            )


@login_required
def new(request):
    if request.method == "POST":
        form = NewNameForm(request.POST)

        if form.is_valid():
            result = service.insert_avenger(
                request, Avenger(id=uuid.uuid4(), name=form.data["avenger_name"])
            )

            if result:
                return HttpResponseRedirect("/heroes/")
            else:
                print("Save failed.")
    else:
        form = NewNameForm(
            data={"avenger_name": "", "avenger_id": "", "disable_save": "null"}
        )
        return render(request, "main_app/name.html", {"myavenger": None, "form": form})

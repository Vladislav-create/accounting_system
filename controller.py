import views
import model


def select_user_menu():
    res = views.user_menu()
    if res == 1:
        views.show_all_animals(model.show_animals())
    elif res == 2:
        model.add_animals_model(views.add_animals())
    elif res == 3:
        views.show_all_animals(model.show_animals())
        model.del_animal_model(views.del_animal())
        views.show_all_animals(model.show_animals())
    else:
        views.show_all_animals(model.show_animals())

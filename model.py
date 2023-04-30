import sqlite3

conn = sqlite3.connect('human_friends.db')
cursor = conn.cursor()


def show_animals():
    cursor.execute("select * from all_animals")
    results = cursor.fetchall()
    return results


def add_animals_model(data):
    print(data)
    name, comands, birthday, typ = data
    print(name, comands, birthday, typ)
    cursor.execute(
        f"insert into all_animals (name, comands, birthday, typ)"
        f"values ('{name}', '{comands}', {birthday}, '{typ}')"
    )
    conn.commit()


def del_animal_model(data):
    cursor.execute(
        f"delete from all_animals where id={data}"
    )
    conn.commit()

   

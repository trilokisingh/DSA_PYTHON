Dict = {"A": "Hello",
        "B": "Nice",
        "C": "Joke",
        "E": "Test"

        }

new_dict={Dict[x]:x for x in Dict}
print(new_dict)
print(type(new_dict))
# Match-case (Python 3.10+)
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Something else")

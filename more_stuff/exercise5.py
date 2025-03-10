def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter          # The bug was global being
        counter += 1              # used on line 5, instead of
                                  # nonlocal.
    
    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
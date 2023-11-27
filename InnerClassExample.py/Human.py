class Human:
    def __init__(self):
        print("In init method")

    class Mouth():
        def __init__(self):
            print("Mount Inner")
        def talk(self):
            print("Human can talk")

        class Brain:
            def __init__(self):
                print("Brain init method")

            def think(self):
                print("HUman brain can think ")


Human().Mouth().Brain().think()
Human().Mouth().talk()                    




class ReadFromInterface:

    def start(self):
        print("ReadFromInterface process has started")

    @staticmethod
    def get_user_input():
        user_input = input("Enter command: ")
        return user_input

class Accident(Exception):  # Accident inherits Exception
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print(f"User defined exception: {self.msg}")

    def handle(self):
        print("An accident occurred, please take a detour.")


if __name__ == '__main__':
    try:
        raise Accident('Crash between two cars')
    except Accident as e:
        # e.print_exception()
        e.handle()
        

import cmd
import json
import os

class KipManagement(cmd.Cmd):

    """This command"""
    
    prompt = "shell $"
    
    def __init__(self):
        super().__init__()
        self.users = {} # list of users
        self.load_from_file()
    
    def do_create(self, line):
        """Creates a new user.
        """
        args = line.split(' ')
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User created - ID: {digit}, Name: {name}")
        else:
            print("Invalid input. syntax: create <digit> <name>")
        self.save_to_file()    
    def do_read(self, line):
        """Read and Display all users"""
        print("list of Chakula")
        for digit, name in self.users.items():
            print(f"ID: {digit}, -> Name: {name}")
        self.save_to_file()
    def do_update(self, line):
        """Update user's name. syntax: create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print("User updated - ID: {digit}, Name: {name}")
            else:
                print("No user found - ID: {digit}, Name: {name}")
        else:
            print("Invalid input. use: <digit> or <name>")
        self.save_to_file() 
    def do_destroy(self, line):
        """Delete a user by ID. syntax: update_<digit> or <name>"""
        if line in self.users:
            del self.users[line]
            print(f"User Deleted - ID: {line}")
        else:
            print(f"No user found with ID {line}")
        self.save_to_file()
        
    def save_to_file(self):
        """ saves data to a file """
        with open("user_data.json", "w") as json_file:
            json.dump(self.users, json_file)
            
    def load_from_file(self):
        """Loads data from a JSON file if it exists."""
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as json_file:
                self.users = json.load(json_file)
        else:
            self.users = {}

            
if __name__ == '__main__':
    KipManagement().cmdloop()
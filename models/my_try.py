#!/usr/bin/env python

import cmd

class Command(cmd.Cmd):
    
    """This command"""
    
    prompt = ">>>"
    
    def do_greet(self, person):
        """Gret the <person>"""
        if person:
                print(f"Hello {person}")
        else:
                print("Hello World!")
                
    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            ]))
        
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True
    
    def default(self, line):
        """Default command"""
        print(f"Unknown command: {line}")
        
    def emptyline(self):
         print("You entered empty line")
         
    def do_quit(self, line):
        """Exits the program.
        """
        return True
    
    def help_quit(self, line):
        print("Quit program")
        
if __name__ == "__main__":
    Command().cmdloop()
    
import cmd

class HelloWorld(cmd.Cmd):
    """ Simple command processor example"""

    FRIENDS = ["Alice", "Adam", "Barbara", "Bob"]

    def do_greet(self, person):
        if person and person in self.FRIENDS:
            greeting = "hi, %s!" % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = "hello"

        print(greeting)

    def help_greet(self):
        print("\n".join(['greet [person]', "Greet the named person",]))

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f for f in self.FRIENDS if f.startwith(text)]
        return completions

    def do_EOF(self, line):
        return True

    def postloop(self):
        print("Exiting the CLI Bye!")

if __name__ == "__main__":
    HelloWorld().cmdloop()

#!/usr/bin/python3

import re
import cmd
import shlex
from models import storage
from models.user import User
from models.song import Song
from models.play_list import Playlist
from models.user_song_interact import UserSongInteraction

classes = {"User": User, "Song": Song, "UserSongInteraction": UserSongInteraction, "Playlist": Playlist}

class GrooveGenie(cmd.Cmd):
    """ implementation of Student Portal class """
    prompt = "(GrooveGenie) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ when you enter an empty line """
        pass

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        
        if not arg:
            print("** class name missing **")
            return False
        
        args = arg.split(' ', 1)  # Split only on the first space to separate class name from the rest
        class_name = args[0]

        if class_name in classes:
            pattern = re.compile(r'(\w+)=["\']?([^"\']+)["\']?')
            new_dict = dict(pattern.findall(args[1]))

            #new_dict = self._key_value_parser(args[1:])
            #print(new_dict)
            instance = classes[args[0]](**new_dict)
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")
            return False

    def tokenize_arg(self, arg):
        """ tokenize argument string """
        try: 
            return shlex.split(arg)
        except ValueError as e:
            print(f"Argument parsing error: {e}")
            return []

    def do_write(self, arg):
        """ Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        new_dict = {}
        if args[0] in classes:
            for arg in args:
                if "=" in arg:
                    key_value = arg.split("=")
                    print(key_value)
                    key = key_value[0]
                    value = key_value[1]
                    new_value = value.replace('"', '')
                    print(new_value)
                    new_dict[key] = new_value
            instance = classes[args[0]](**new_dict)
            print(instance.id)
            instance.save()
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ return all class attributes """
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = storage.all(classes[args[0]])
        else:
            print("*** class name missing ***")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

if __name__ == '__main__':
    GrooveGenie().cmdloop()

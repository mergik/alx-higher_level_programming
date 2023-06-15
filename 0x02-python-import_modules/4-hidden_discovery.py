#!/usr/bin/python3
import dis
import marshal
import sys
import types

if __name__ == "__main__":
    module_name = "hidden_4"

    # Load the compiled code object from the pyc file
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)  # Read the magic number
        timestamp = file.read(4)  # Read the timestamp
        compiled_code = marshal.load(file)  # Load the compiled code object

    # Create a temporary module to execute the code object
    compiled_module = types.ModuleType(module_name)
    exec(compiled_code, compiled_module.__dict__)

    # Get the defined names in the compiled module
    defined_names = sorted(
        name for name in dir(compiled_module) if not name.startswith("__")
    )

    # Print the defined names
    for name in defined_names:
        print(name)

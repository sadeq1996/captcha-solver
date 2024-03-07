
# - - - - - - - - IN-BUILT IMPORTS

import os
from traceback import format_exc
from shutil import copy2
from clr import CompileModules

# - - - - - - - - CLASS LIBRARY

class Compiler:

    @staticmethod
    def collect_files(folder_path):
        """Collects relevant python script files.
        Args:
            folder_path (str): Root directory to collect_files.
        Returns:
            list(str): List of absolute file paths.
        """
        files = []
        # Ignore the current file, and files named '__init__.py'. Add other names if required.
        ignore_list = (os.path.basename(__file__), "__init__.py", "local", "bin")

        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                abs_path = os.path.join(folder_path, file)
                # ignore from ignore_list.
                if not file in ignore_list and file.endswith(".py"):
                    files.append(abs_path)
                # Recursiion for sub-folders
                elif os.path.isdir(abs_path) and file.lower() not in ignore_list:
                    files += Compiler.collect_files(abs_path)
        
        return files
    
    @staticmethod
    def Build(filename, source_folder = "", copy_target = "", export_folder = "bin"):
        """Collects and compiles project files into a dll.
        Args:
            filename (str): Name of final output (.dll) file.
            source_folder (str): (optional) Folder to collect files from.
            copy_target (str) : (optional) File path to where the output needs to be copied.
            export_folder (str): Subfolder for output file.
        Returns:
            (bool) True if successful, False otherwise.
        """
        folder_name = os.path.dirname(os.path.abspath(__file__))
        source_folder = os.path.join(folder_name, source_folder)
        target_folder = os.path.join(folder_name, export_folder)
        target_file = os.path.join(target_folder, filename)

        # Create export folder.
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # Collect necessary files from project folder.
        program_files = Compiler.collect_files(source_folder)

        try:
            CompileModules(target_file, *program_files)
            print("\nBUILD SUCCESSFUL\nTarget: {}\n".format(target_file))
            
            # Copy output file to user specified location.
            if copy_target and os.path.exists(copy_target):
                copy2(target_file, copy_target)
                print("COPY SUCCESSFUL\n")
            
            return True

        except ImportError:
            print("\nBUILD FAILED\n\nPlease run the script using IronPython.\nRefer docstrings for more information.\n")

        except Exception as ex:
            print("\nBUILD FAILED\n")
            print(format_exc())
            print(str(ex))
            return False

# - - - - - - - - RUN SCRIPT

def Run():
    print(os.path.abspath(__file__))
    Compiler.Build("my_module.dll")

if __name__ == "__main__":
    Run()
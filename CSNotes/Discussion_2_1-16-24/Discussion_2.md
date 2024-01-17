If your mypy or python3 is not installed in the correct PATH, you can change the path by exporting it in the terminal session or change for every following terminal session by changing it in the bashrc file, running the export command to fix the problem.

installing packages usually or almost always installs on the user's home directory, not the system directory, as other users may not need or want those same packages. Some applications only run with certain packages, or don't run at all with the wrong packages.

One solution to this is to always use virtual environments, having select packages for the virtual environment each time. Virtual enviroments should be used per project or assignment.

do this by running in the project directory/repository.

python3 venv venv

Activate environment: (Windows) source venv/bin/activate
deactivate environment: deactivate.

One of the use cases of this is to run select packages for AI stuff from older versions, because many researchers don't update their code/packages.
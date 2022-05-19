import pathlib

PATH = pathlib.Path(__file__).parent
# PATH_FOLDER = PATH.join
PATH_FOLDER = PATH.joinpath('../datasets').resolve()
PATH_FOLDER_FILE = PATH_FOLDER.joinpath('empresasTech.csv').resolve()
print(PATH_FOLDER_FILE)

print('test')
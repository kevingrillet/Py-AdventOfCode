import os.path
import shutil


def replace_in_file(year: str, path: str):
    f = open(path, 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace('XXXX', new)

    f = open(path, 'w')
    f.write(newdata)
    f.close()


if __name__ == '__main__':
    new = '2017'

    if not os.path.exists('../' + new):
        shutil.copytree('./year/', '../' + new)

    replace_in_file(new, '../' + new + '/README.md')
    replace_in_file(new, '../' + new + '/main.py')

    for i in range(25):
        day = "{:02d}".format(i + 1)
        if not os.path.exists('../' + new + '/' + day):
            shutil.copytree('./day/', '../' + new + '/' + day)

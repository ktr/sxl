
import fileinput
import re
import os
from subprocess import Popen, PIPE, STDOUT, check_output
import sxl

def here():
    return os.path.dirname(__file__)

def get_current_version():
    return sxl.__version__


def get_new_version(version, bump_type):
    assert bump_type in ('major', 'minor', 'patch', 'pre-release')
    bumper = {
        'major' : 0,
        'minor' : 1,
        'patch' : 2,
        'pre-release' : 3,
    }
    idxs = [0, 1, 2, 5]
    # major, minor, patch, pre-release (alpha, beta, release candidate)
    version_re = re.compile(r'(\d+).(\d+).(\d+)(([abrc]{1,2})(\d+))?')
    gps = version_re.match(version).groups()
    vals = [int(gps[idx]) for idx in idxs]
    vals[bumper[bump_type]] += 1
    vals = [str(_) for _ in vals]
    return vals[0] + '.' + vals[1] + '.' + vals[2] + gps[4] + vals[3]


def bump(old_version, new_version):
    filenames = ('./sxl/__init__.py', './setup.py')
    for filename in filenames:
        with fileinput.FileInput(filename, inplace=True, backup='.bak') as infile:
            for line in infile:
                print(line.replace(old_version, new_version), end='')


def deploy():
    # setup = os.path.join(here(), 'setup.py')
    check_output(['python', 'setup.py', 'sdist'])
    check_output(['python', 'setup.py', 'bdist_wheel'])
    # check_output(['twine', 'upload', 'dist/*'], stdin=PIPE)
    # p = Popen(['twine', 'upload', 'dist/*'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # stdout, stderr = p.communicate("this is some input")


if __name__ == "__main__":
    old = get_current_version()
    new = get_new_version(old,'pre-release')
    cur = old
    cont = input("Bumping {} -> {}\nContinue (Y/N)? ".format(old, new))
    if cont.lower().startswith('y'):
        bump(old, new)
        cur = new
        print("Bumped")
    else:
        print("Did not bump")
    cont = input("Deploy to pypi (Y/N)? ")
    if cont.lower().startswith('y'):
        deploy()
        print("Bult distros for PyPi. Now run:\n" +
              "twine upload dist/sxl-{}-py3-none-any.whl\n".format(cur) +
              "twine upload dist/sxl-{}.tar.gz\n".format(cur))
    else:
        print("Did not upload to PyPi")

#!/usr/bin/env bash

#enable script exit when 1st error occurs
set -e


#must to sudo or root user to run this script
if [[ $EUID -ne 0 ]]; then
   echo "*** This script must be run as root" 1>&2
   exit 1
fi

#
python='/opt/ActivePython-2.7/bin/python'
expected_pip_version='*pip 9.*'

function echoerr() { echo "$@" 1>&2; }

function get_python_version() {
    ver=$($python --version 2>&1)
    echo $ver
}

function get_pip_version() {
    ver=$($python -m pip -V 2>&1)
    echo $ver
}

function pip_upgrade {
    #create temp directory and cd into it.
    cd $(mktemp -d)
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py
    chmod 777 get-pip.py
    chmod 777 /opt/ActivePython-2.7 -R
    /opt/ActivePython-2.7/bin/python get-pip.py
}

function cafe_sanity_check() {
    echo ""
    echo "*** santiy check on python packages installed"
    echo ""

    #use rpyc & ncclient import to verify if the pypm/pip python packages repository get corrupted
    rpyc_ver=$($python -c 'import rpyc; print rpyc.__version__' 2>&1)
    echo "*** rpyc version==$rpyc_ver"
    if [[ $rpyc_ver =~ \([0-9]\,\ [0-9]\,\ [0-9]\) ]]; then
        echo "*** able to import rpyc"
    else
        echoerr "*** unable to import rpyc, please contact Cafe dev team for further assistance"
        exit 1
    fi
    ncclient_ver=$($python -c 'import ncclient; print ncclient.__version__' 2>&1)
    echo "*** ncclient version==$ncclient_ver"
    if [[ $ncclient_ver == \([0-9]\,\ [0-9]\,\ [0-9]\) ]]; then
        echo "*** able to import ncclient"
    else
        echoerr "*** unable to import ncclient, please contact Cafe dev team for further assistance"
        exit 1
    fi
    echo ""
    echo "*** sanity check completed"
}


#
x=$(get_pip_version)
echo $x
#check if pip upgrade is needed
if [[ $x == $expected_pip_version ]]; then
    echo "*** Expected python package manager version is already installed"
    echo "*** No upgrade is needed"
    cafe_sanity_check
    exit 0
else
    echo "Start pip upgrade ...."
fi

#......
pip_upgrade

#check if upgrade is good
x=$(get_pip_version)
echo $x

if [[ $x == $expected_pip_version ]]; then
    echo "*** pip upgrade compeleted"
else
    echoerr "*** pip upgrade FAILED"
fi

#sanity check of the cafe python packages
cafe_sanity_check
echo ""
echo "DONE!!!"
echo ""


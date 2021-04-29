#!/bin/bash
    
echo "Log: Installing Python 3.6"
amazon-linux-extras install python3

echo "Log: Checking python installed properly or not"

python3 --version

echo "Log: upgrading pip"
pip3 install  --no-input --upgrade pip

PY_INSTALLED=$?
echo "Log: result of Install_Python.sh is ${PY_INSTALLED} .0=success 1=failure."
if [[ ${PY_INSTALLED} -gt 0 ]];
then
   exit 1
fi

echo "Log: Installing psycopg2 dependencies - Start"
echo "Log: Installing deltarpm"
yum -y -q install deltarpm 
echo "Log: Installing postgresql"
yum -y -q install postgresql 
echo "Log: Installing postgresql-devel"
yum -y -q install postgresql-devel 
echo "Log: Installing python-devel"
yum -y -q install python-devel 
echo "Log: Installing python3-devel"
yum -y -q install python3-devel 
echo "Log: Installing postgresql-libs"
yum -y -q install postgresql-libs
echo "Log: Installing gcc"
yum -y -q install gcc

echo "Log: Installing necessary packages from requirements.txt"
pip3 install --no-input -r requirements.txt
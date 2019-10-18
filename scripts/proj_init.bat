set arg1=%1
cd %1
python proj_init.py

py -m venv env

code .

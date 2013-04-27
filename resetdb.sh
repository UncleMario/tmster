#!/bin/sh

sudo -u postgres dropdb tmster
sudo -u postgres createdb tmster
python manage.py syncdb --settings tmster.localsettings
python manage.py runserver --settings tmster.localsettings

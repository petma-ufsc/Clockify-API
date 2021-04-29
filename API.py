
import requests
import numpy
from pandas import json_normalize
import json
import datetime
from orator import DatabaseManager, Model, Schema
from models import *

now = datetime.datetime.now()
time_interval = now - datetime.timedelta(weeks=40)


Member.save_from_clockify()
Category.save_from_clockify()
Project.save_from_clockify()
Activity.save_from_clockify()
TimeEntry.save_from_clockify(start=time_interval.strftime('%Y-%m-%dT%H:%M:%SZ'))
import os

DEBUG = True

# no duplicate values
ADMINS = frozenset([os.environ.get('ADMIN_EMAIL')])
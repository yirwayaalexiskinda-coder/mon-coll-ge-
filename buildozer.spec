[app]

# (str) Title of your application
title = Ma candidature

# (str) Package name
package.name = monapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source file where the main.py file exists
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude nothing)
#source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
# Valid options are: landscape, portrait, all-sensor, sensor
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

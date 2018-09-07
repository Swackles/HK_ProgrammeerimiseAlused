@echo off

SET _directory=%cd%
SET _file=\Menu.py

SET _location=%_directory%%_file%

SET _result=%_location:\=//%

python %_result%
# Annotator

## Run

`pip3 install -r requirement.txt`

`python3 manage.py runserver`

## How it works

There are 3 variables `data_dir`, `dump_file` and `log_file` defined in `me_annotate/views.py`. Users can select the data which he want to annotate from `data_dir`. The dumped database will be stored in `dump_file` and the log file will be stored in `log_file`. These 3 variables are corresponding to environment variables `DATA`, `DUMP` and `LOG` respectively

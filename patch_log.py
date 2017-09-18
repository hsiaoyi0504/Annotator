import os
import json
log_file = os.getenv('LOG') if os.getenv('LOG') != None else 'log'
if os.path.isfile(log_file) :
    log = json.load(open(log_file, 'r'))

dump_file = os.getenv('DUMP') if os.getenv('DUMP') != None else 'annotation.json' 
if os.path.isfile(dump_file) :
    db_raw = json.load(open(dump_file, 'r'))
    
    db_raw = json.loads(db_raw)


def update_log(new_key, new_value):
    '''
    Update the log file,
    just for designer 
    '''
    for key, value in log.items():
        if type(value) != dict:
            continue
        if key not in value.keys():
            log[key][new_key] = new_value

if __name__ == '__main__':
    
    update_log('completed', False)
    

    for key, value in log.items():
        if type(value) != dict:
            continue
        log[key]['annotated'] = 0
    for record in db_raw:
        uri = record['fields']['uri']
        filename = uri.split('/')[-1]
        if filename in log.keys():
            log[filename]['annotated'] += 1


    json.dump(log, open(log_file, 'w'))
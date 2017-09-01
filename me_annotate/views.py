from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core import serializers
import annotator

import os
import json
import datetime

data_dir = os.getenv('DATA') if os.getenv('DATA') != None else 'tmp'
dump_file = os.getenv('DUMP') if os.getenv('DUMP') != None else 'annotation.json' 
log_file = os.getenv('LOG') if os.getenv('LOG') != None else 'log'

if os.path.isfile(log_file) :
    log = json.load(open(log_file, 'r'))
else:        
    log = {'latest_dump': 'None'}

def paper_annotate(request, paper_name):
    '''
    Paper annotation entry point
    '''
    log[paper_name]['visited'] += 1
    file = os.path.join(data_dir, paper_name)
    texts = []
    with open(file, 'r') as f:
        for line in f:
            texts.append({'text':line})
    return render(request, 'paper.html', {'texts': texts})


def dump_db(request):
    '''
    Dump all db to dump_file
    '''
    qs = annotator.models.Annotation.objects.all()
    qs_json = serializers.serialize('json', qs)
    json.dump(qs_json, open(dump_file, 'w'))

    log['latest_dump'] = str(datetime.datetime.now())
    return redirect(reverse('index'))

def index(request):
    '''
    Scan data_dir and display file names
    '''
    files = [name for name in os.listdir(data_dir) if not name.startswith(".")]
    papers, texts = [], []
    for file in files:
        try:
            gene, variance = file.split('with')
        except:
            gene, variance = '<unk>', '<unk>'
        if file not in log.keys():
            log[file] = { 'name': file,
                          'visited':0,
                          'gene': gene,
                          'variance': variance
                          }
        papers.append(log[file])

    json.dump(log, open(log_file, 'w'))
    return render(request, 'index.html', {'papers':papers, 'latest_dump':log['latest_dump']})
        
        

class DemoView(TemplateView):
    template_name = "demo.html"


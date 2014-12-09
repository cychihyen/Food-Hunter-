#coding=utf-8
from __future__ import division
from operator import itemgetter
import json #or cjson
import re
import sys
from django.http import HttpResponse
from django.shortcuts import render_to_response

class Project(object): 

    def __init__(self):
        pass

    @staticmethod
    def read_line(a_json_string_from_document):
        return json.loads(a_json_string_from_document)

    @staticmethod
    def tokenize(string):
        string = string.lower()
        list = re.findall('\w+', string)
        list = [str(x) for x in list]
        return list

    @staticmethod
    def comp(list1, list2):
        for word1 in list1:
            for word2 in list2:
                if word1 == word2: # and word1 in ingredient file
                    return 1
  
        return 0

    def cosine(self, query_list, data_list):
        query_list = [self.tokenize(word) for word in query_list]
        data_list = [self.tokenize(word) for word in data_list]

        numerator = 0
        denominator = 0
        for q in query_list:
        	for d in data_list:
        		numerator += self.comp(q, d)
    
        denominator = (len(query_list)**0.5) * (len(data_list)**0.5)

        if denominator != 0:
            return numerator / denominator
        else:
            return 0


top = []

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    query_list = []

    count = 1
    while ('i' + str(count)) in request.GET:
		query_list.append(str(request.GET['i' + str(count)]))
		count += 1

    inputfile = "/Users/Chih-YenChang/Documents/database.json"
    f=open(inputfile, 'r')

    dict = {}
    proj = Project()
    while 1:
        line = f.readline()
        if not line:
            break
        for i in range(10):
            data = Project.read_line(line)['matches'][i]
            data_list = data['ingredients']
            for x in data_list:
            	x.encode("utf-8","ignore")

            id = str(data['id'])
            #for ing in data['ingredients']:
             #   ing.encode("utf-8", "ignore")
            #data['ingredients'] = data_list

            if dict.has_key(id):
                dict[id] = (proj.cosine(query_list,data_list), data)
            else:
                dict[id] = (proj.cosine(query_list,data_list), data)

    top = sorted(dict.items(), key=lambda x: x[1][0], reverse=True)

    top = [ x[1][1] for x in top]

    return render_to_response('result.html', {'result': top[:10]})


def result(request, pagenumber):
    html = "<html><body>In %s (s).</body></html>" % (pagenumber)
    return HttpResponse(html)


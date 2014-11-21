from __future__ import division
from operator import itemgetter
import json #or cjson
import re
import sys

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
                else:
        		    return 0

    def cosine(self, query_list, data_list):
        query_list = [Project.tokenize(word) for word in query_list]
        data_list = [Project.tokenize(word) for word in data_list]

        numerator = 0
        denominator = 0
        for q in query_list:
        	for d in data_list:
        		numerator += Project.comp(q, d)
    
        denominator = (len(query_list)**0.5) * (len(data_list)**0.5)

        if denominator != 0:
            return numerator / denominator
        else:
            return 0

if __name__ == '__main__':
    query_list = ['beef','tomato']

    inputfile = 'database.json'
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
            proj.cosine(query_list,data_list)
            id = data['id']
            if dict.has_key(id):
                print "same id", id
                dict[id] = (proj.cosine(query_list,data_list), data)
            else:
                dict[id] = (proj.cosine(query_list,data_list), data)

    top = sorted(dict.items(), key=lambda x: x[1][0], reverse=True)

    for i in top[:5]:
        print i

        		

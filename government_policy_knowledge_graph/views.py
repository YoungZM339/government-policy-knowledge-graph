import json

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from neo4j_db.edit_graph import query, get_qa_system_answer, get_answer_profile, add_relation_graph, query_all_objects, \
    del_object, query_content
from qa_system.ltp import get_target_array


def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def qa_system(request):
    return render(request, 'qa_system.html')


def all_relation(request):
    return render(request, 'all_relation.html')


def edit_relation(request):
    return render(request, 'edit_relation.html')


def get_profile(request):
    request_data = request.GET
    name = request_data.get('character_name')
    json_data = get_answer_profile(name)
    return JsonResponse(json_data)


def qa_system_answer(request):
    request_data = request.GET
    question = request_data.get('name')
    json_data = get_qa_system_answer(get_target_array(str(question)))
    return JsonResponse(json_data)


def search_name(request):
    request_data = request.GET
    name = request_data.get('name')
    json_data = query(str(name))
    return JsonResponse(json_data)


def search_all_objects(request):
    json_data = query_all_objects()
    return JsonResponse(json_data)


def add_relation(request):
    request_data = request.GET
    obj1 = request_data.get('obj1')
    obj2 = request_data.get('obj2')
    relation = request_data.get('relation')
    data = [obj1, obj2, relation]
    json_data = add_relation_graph(data)
    return JsonResponse(json_data)


def del_relation(request):
    request_data = request.GET
    obj = request_data.get('obj')
    json_data = del_object(obj)
    return JsonResponse(json_data)


def display_policy_content(request):
    request_data = request.GET
    name = request_data["name"]
    # content_data = {"policy_content": query_content(name)}
    with open("./raw_data/content.json", encoding='utf-8') as f:
        json_data = json.load(f)
        for i in json_data["data"]:
            if i["name"] == name:
                content_data = {"policy_content": i["content"]}
                break
    return render(request, 'policy_content.html', content_data)

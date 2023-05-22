from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from neo4j_db.edit_graph import query, get_qa_system_answer, get_answer_profile, add_relation_graph, query_all_objects, \
    del_object
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


def search_all_objects():
    json_data = query_all_objects()
    return JsonResponse(json_data)


def add_relation(request):
    request_data = request.GET
    obj1 = request_data.get('obj1')
    obj2 = request_data.get('obj2')
    relation = request_data.get('relation')
    cate1 = request_data.get('cate1')
    cate2 = request_data.get('cate2')
    data = [obj1, obj2, relation, cate1, cate2]
    json_data = add_relation_graph(data)
    return JsonResponse(json_data)


def del_relation(request):
    request_data = request.GET
    obj = request_data.get('obj')
    del_object(obj)
    return JsonResponse([{"code": 1}])

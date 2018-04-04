from collections import deque


def person_is_doctor(person):
    return person[-1] == 'm'


def search(name):
    graph = dict()
    search_queue = deque()
    search_queue += graph['name']
    searched = list()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_doctor(person):
                print('find the doctor nearest!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
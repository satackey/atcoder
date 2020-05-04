from sys import stderr
import json

def debug(*args):
    print(*args, file=stderr)

n_observatory_num, m_roads_num = map(int, input().split())
hi_heights = list(map(int, input().split()))

ab_roads_fromto = [map(int, input().split()) for _ in range(m_roads_num)]


class ObservatoryController():
    observatories_by_id = {}

    def add(self, a_observatory):
        self.observatories_by_id[a_observatory.id] = a_observatory

    def connect_by_id(self, a_id, b_id):
        observatory_a = self.observatories_by_id[a_id]
        observatory_b = self.observatories_by_id[b_id]

        observatory_a.connect_to(observatory_b)
        observatory_b.connect_to(observatory_a)

    
    def count_good_observatories(self):
        result = 0
        for id, a_observaotry in self.observatories_by_id.items():
            if a_observaotry.is_good():
                result += 1
        return result


class Observatory():
    def __init__(self, id, height):
        self.id = id
        self.height = height
        self.connected_to_by_id = {}

    def __repr__(self):
        construct = json.dumps({
            'id': self.id,
            'height': self.height,
        })
        return "<Observatory '%s'>" % (construct)

    def connect_to(self, a_observaotry):
        self.connected_to_by_id[a_observaotry.id] = a_observaotry

    def is_good(self):
        for a_connected_observatory in self.connected_to_by_id.values():
            if self.height <= a_connected_observatory.height:
                return False
        return True

observatoryController = ObservatoryController()

for i, height in enumerate(hi_heights):
    id = i + 1
    observatory = Observatory(id, height)
    observatoryController.add(observatory)

for a, b in ab_roads_fromto:
    observatoryController.connect_by_id(a, b)

result = observatoryController.count_good_observatories()

print(result)

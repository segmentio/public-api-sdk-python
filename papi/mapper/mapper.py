import json
import queue
from ..common import Object


def tojsonstr(obj, pretty_print=True):
    indent = 5 if pretty_print else None
    return json.dumps(obj, default=object_serializer, indent=indent)


def object_serializer(obj):
    attributes = obj.__dict__.copy()
    rename_array = attributes.pop('__rename', None)
    if rename_array:
        for key, value in rename_array.items():
            attributes[value] = attributes[key]
            attributes.pop(key, None)
    return attributes


class QueueItem:
    pass


def SetAppendValue(item, value):
    if item.parent is not None:
        if isinstance(item.parent.value, list):
            item.parent.value.append(value)
        else:
            setattr(item.parent.value, item.id, value)
    else:
        item.value = value


def fromjsonstr(data):

    if not data:
        return data

    root = QueueItem()
    root.node = json.loads(data)  # pylint: disable=W0201
    root.parent = None  # pylint: disable=W0201
    root.value = None  # pylint: disable=W0201

    q = queue.Queue()
    q.put(root)
    while not q.empty():
        item = q.get()
        if item.node is None:
            SetAppendValue(item, None)
        elif isinstance(item.node, (int, float, bool, str)):
            SetAppendValue(item, item.node)
        elif isinstance(item.node, list):
            item.value = []
            SetAppendValue(item, item.value)
            for kidnode in item.node:
                kid = QueueItem()
                kid.parent = item  # pylint: disable=W0201
                kid.node = kidnode  # pylint: disable=W0201
                q.put(kid)
        elif isinstance(item.node, dict):
            item.value = Object()
            SetAppendValue(item, item.value)
            for kidnode, kidvalue in item.node.items():
                kid = QueueItem()
                kid.parent = item  # pylint: disable=W0201
                kid.id = kidnode  # pylint: disable=W0201
                kid.node = kidvalue  # pylint: disable=W0201
                q.put(kid)

    return root.value

import os
import json,re

BASE = os.path.dirname(os.path.abspath(__file__))

class  Transform(object):
    def __init__(self,paths,items,extends):
        super(Transform,self).__init__()
        self.paths = paths
        self.items = items
        self.extends = extends
        pass

    @classmethod
    def create(cls,source):
        paths = source["paths"]
        _paths = []
        for pathpart in paths:
            __path = BASE
            for item in pathpart:
                __path = os.path.join(__path,item)
            _paths.append(__path)

        items = source["items"]
        _items = []
        for item in items:
            _items.append(Item.create(item))
        return cls(_paths,_items,source["extends"])

class Item(object):
    def __init__(self,key,value):
        super(Item,self).__init__()
        self.key = key
        self.value = value
    @classmethod
    def create(cls,item):
        return cls(item["key"],item["value"])


class Factory(object):
    def __init__(self,transform):
        super(Factory,self).__init__()
        self.transform = transform

    def FileTransform(self,target):
        Source = ""
        print(target)
        with open(target,"r+") as file:
            Source = file.read()
        
        with open(target,"w+") as file:
            
            for item in self.transform.items:
                key = item.key
                value = item.value
                Source =  Source.replace(key,value)
            file.write(Source)
            
        pass

    def _StartTransform(self,source):
        if os.path.isfile(source):
            self.FileTransform(source)
            pass
        elif os.path.isdir(source):
            files = os.listdir(source)
            filesP = [os.path.join(source,name) for name in files]
            for file in filesP:
                for extend in self.transform.extends:
                    if file.endswith(extend):
                        self._StartTransform(file)
                        break
                    pass
            pass
        pass
    def StartTransform(self):
        if isinstance(self.transform,Transform):
            paths = [os.path.join(BASE,path) if not (os.path.isdir(path) or os.path.isfile(path)) else path for path in self.transform.paths]
            for  target in paths:
                self._StartTransform(target)
                pass
            pass
        pass


if __name__ == "__main__":
    jsonfile = os.path.join(BASE,"transform.json")
    with open(jsonfile,"r+") as transform :
        target = json.load(transform)
        transform = Transform.create(target)
        fan = Factory(transform)
        fan.StartTransform()
    pass
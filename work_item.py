
class WorkItem:
    __id = None
    _descriptor = None
    _args = None
    _kwargs = None

    def __init__(self, id, descriptor, args=None, kwargs=None):
        self.__id = id
        self._descriptor = descriptor
        self._args = args
        self._kwargs = kwargs

    @property
    def id(self):
        return self.__id

    @property
    def descriptor(self):
        return self._descriptor

    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs


class WorkResultItem:
    _work_item = None
    _result = None

    def __init__(self, work_item, result):
        self._work_item = work_item
        self._result = result

    @property
    def work_item(self):
        return self._work_item

   @property
   def result(self):
       return self._result

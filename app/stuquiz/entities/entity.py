# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23


class Entity(object):
    def dump(self) -> dict:
        return dict(self.__dict__)

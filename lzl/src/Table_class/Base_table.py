import abc


class Base_table(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, col_name, datas):
        for key in Base_table.__dict__:
            if key != '_':
                print(key + ":" + Base_table.__dict__[key])

    @abc.abstractmethod
    def write(self, file):
        d = Base_table.__dict__
        for key in d:
            file.write(d[key])

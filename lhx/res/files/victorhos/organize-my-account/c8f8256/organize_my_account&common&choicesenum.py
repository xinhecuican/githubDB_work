from choicesenum import ChoicesEnum


class ChoicesEnum(ChoicesEnum):

    @classmethod
    def choices(cls):
        return [(choices.value, choices.display) for choices in cls]

    @classmethod
    def get_database_max_length(cls):
        return max(len(item.value) for item in cls)

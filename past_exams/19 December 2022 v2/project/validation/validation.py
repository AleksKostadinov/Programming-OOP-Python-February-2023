class Validation:
    @staticmethod
    def empty_string_or_white_space(value, message):
        if len(value) == 0 or value.isspace():
            raise ValueError(message)

    @staticmethod
    def age_less(value, message):
        if value < 16:
            raise ValueError(message)

    @staticmethod
    def check_not_in(value, values, message):
        if value not in values:
            raise ValueError(message)

    @staticmethod
    def check_in(value, values, message):
        if value in values:
            raise ValueError(message)

    @staticmethod
    def check_for_empty_string(value, message):
        if len(value) == 0:
            raise ValueError(message)

    @staticmethod
    def check_number_less_than(value, number_to_be_less,  message):
        if value < number_to_be_less:
            raise ValueError(message)

    @staticmethod
    def check_if_string_is_less_than(value, message):
        if len(value.strip()) < 2:
            raise ValueError(message)

    @staticmethod
    def check_for_duplicity(search_for: str, objects: list, attrib_check: str, message: str):
        if any(getattr(i, attrib_check) == search_for for i in objects):
            raise Exception(message)

    @staticmethod
    def check_if_object_with_given_name_exists(name: str, message: str):
        if name is None:
            raise Exception(message)

    @staticmethod
    def check_band_one_of_each_type_musician(message: str):
        raise Exception(message)

    @staticmethod
    def check_band_members_have_the_skills(members: list, all_members: list, message: str):
        if len(members) != len(all_members):
            raise Exception(message)





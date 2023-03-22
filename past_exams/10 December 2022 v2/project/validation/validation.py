class Validation:
    @staticmethod
    def empty_string_or_white_space(value, message):
        if value.strip() == '':
            raise ValueError(message)

    @staticmethod
    def price_less_or_equal_0(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def capacity_less_0(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def duplicates_name(name, delicacies_list, message):
        # for delicacy in delicacies_list:
        #     if delicacy.name == name:
        #         raise Exception(message)
        if any(name == x.name for x in delicacies_list):
            raise Exception(message)

    @staticmethod
    def duplicates_num(num, booths_list, message):
        if any(num == x.booth_number for x in booths_list):
            raise Exception(message)

    @staticmethod
    def not_valid_type(type_, correct_type, message):
        if type_ not in correct_type:
            raise Exception(message)

    @staticmethod
    def not_found(item, message):
        if not item:
            raise Exception(message)






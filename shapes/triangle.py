
class Triangle:

    def __init__(self, angle_val, name_val):
        setattr(self, 'angles', angle_val)
        self.name = name_val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self.validate_name(value)

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, value):
        self._angles = Triangle.validate_num(value)

    @staticmethod
    def validate_num(value=None):
        if value and type(value) == list:
            if len(value) != 3:
                raise ValueError('Input list must have exactly 3 entries')
            else:
                if any(not i or not isinstance(i, (int, float)) or i <= 0 for i in value):
                    raise ValueError('List entries must be a real number greater than zero')
                else:
                    if abs(sum(value)-180) >0.01:
                        raise ValueError('Sum of angles must be 180')
                    else:
                        return value
        else:
            raise ValueError('Input must be a list')

    @staticmethod
    def validate_name(value):
        if type(value) == str:
            if value.strip():
                return value
            else:
                raise ValueError('Input must contain 1 or more character')
        else:
            raise ValueError('Input must be a string')

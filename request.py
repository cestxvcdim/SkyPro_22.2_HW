
class Request:
    def __init__(self, request):
        self._string = request.split()
        self._from_place = self._string[4]
        self._to_place = self._string[6]
        self._amount = self._string[1]
        self._product = self._string[2]

    @property
    def from_place(self):
        return self._from_place

    @property
    def to_place(self):
        return self._to_place

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

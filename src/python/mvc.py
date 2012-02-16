class AlphaView(object):
    def __init__(self, model):
        self._model = model
        self.update()

    def update(self):
        self._display = 'I have shiny new data! Here: {}'.format(self._model.data)

    def __str__(self):
        return self._display

class AlphaModel(object):
    def __init__(self, data_series):
        """
        data_series: must be iterable.
        """
        self._data = data_series
        self._index = 0

    def service(self):
        # Cycle through the data.
        self._index += 1
        if self._index >= len(self._data):
            self._index = 0

    @property
    def data(self):
        return self._data[self._index]

class AlphaController(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def on_event(self):
        self._model.service()
        self._view.update()



#################################
# Tests
#


def _test_alpha():
    expected_data = 'abcdefghijklmnop'
    model = AlphaModel(expected_data)
    view = AlphaView(model)
    controller = AlphaController(model, view)
    for index in xrange(0, len(expected_data)):
        print view
        assert str(view).endswith(expected_data[index])
        controller.on_event()


def _test_all():
    _test_alpha()

if __name__ == '__main__':
    _test_all()












"""
Simplified MVC examples.
"""


##
# The Alpha MVC illustrates the canonical example where the controller references the model and view directly.
##

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
        self._cycle = Cycle(data_series)

    def service(self):
        self._cycle.next()

    @property
    def data(self):
        return self._cycle.current

class AlphaController(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def on_event(self):
        self._model.service()
        self._view.update()

class Cycle(object):
    """
    Cycle through data elements. Not part of MVC but underpins our model.
    """
    def __init__(self, data_series):
        """
        data_series: must implement __getitem__
        """
        self._data = data_series
        self._index = 0

    def next(self):
        #
        self._index += 1
        if self._index >= len(self._data):
            self._index = 0

    @property
    def current(self):
        return self._data[self._index]

##
# The Beta MVC illustrates using an observer to decouple the controller from the model and view.
##


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












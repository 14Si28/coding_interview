"""
Simplified MVVM ( Model View ViewModel ) example.
MVVM is a pattern commonly used in .NET WPF, a specialization of MVP, PM, and its variants.
This pattern is almost never used in Python; this is an illustration.
"""

class Model(object):
    def __init__(self, view_model):
        self._view_model = view_model
        self.data = None

    def update(self, model_data):
        print 'Model updated.'
        self.data = model_data
        print 'Model notifying ViewModel...'
        self._view_model.on_model_update()

class View(object):
    def __init__(self, view_model):
        self._view_model = view_model

    def on_event(self, event_data):
        print 'View notifying ViewModel...'
        self._view_model.on_view_event(event_data)

    def on_model_update(self):
        # View logic is kept to a minimum. The ViewModel handles data transformation and possibly rendering.
        # The view becomes just a way to display the ViewModel's presentation  of data.
        print 'View updated: {}'.format(self)

    def __str__(self):
        return self._view_model.data

class ViewModel(object):
    def __init__(self):
        self.model = None
        self._model_observers = []

    def add_model_observer(self, observer):
        if not observer:
            raise ValueError('observer cannot be None')
        self._model_observers.append(observer)

    def on_view_event(self, event_data):
        print 'ViewModel updating model...'
        self._check_model()
        # Convert the event_data into something the model understands.
        model_data = str(event_data)
        # Manipulate the model.
        self.model.update(model_data)
        # No explicit event notification here.

    def on_model_update(self):
        print 'ViewModel notifying model observers...'
        for obs in self._model_observers:
            obs.on_model_update()

    def _check_model(self):
        if not self.model:
            raise ValueError('model not initialized.')

    @property
    def data(self):
        self._check_model()
        # Convert the model's data into a displayable form.
        return str(self.model.data)


#################################
# Tests
#

def _test_all():
    view_model = ViewModel()
    model = Model(view_model)
    view_model.model = model
    view = View(view_model)
    view_model.add_model_observer(view)
    print view
    assert str(view) == 'None'
    input = ['One', 'Two', 'Three']
    for expected in input:
        model.update(expected)
        assert str(view) == expected
        print view

    print
    expected = '888'
    view.on_event(expected)
    print view
    assert str(view) == expected

if __name__ == '__main__':
    _test_all()

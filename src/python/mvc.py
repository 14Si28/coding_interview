"""
Simplified MVC examples.
"""


##
# The Passive MVC illustrates a passive model: the model has no way of notifying view of data changes.
# The controller must notify the view of changes to the model.
##

class PassiveView(object):
    def __init__(self, model):
        self._model = model
        self.update()

    def update(self):
        self._display = 'I have shiny new Passive data! Here: {}'.format(self._model.data)

    def __str__(self):
        return self._display

class PassiveModel(object):
    def __init__(self, data_series):
        self._cycle = Cycle(data_series)

    def service(self):
        self._cycle.next()

    @property
    def data(self):
        return self._cycle.current

class PassiveController(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def on_event(self):
        self._model.service()
        self._view.update()

##
# The Active MVC illustrates an active model that changes independently of the controller.
# An observer is used to decouple the model from the view and controller.
#
# For clarity, some code in this illustration is duplicated with the Passive MVC.
##

# Interfaces in python are debatable, but usually overkill.
# In this case, it's purely for illustration, since duck typing 
# gets us to the same place without the extra interface.
class ActiveObserver(object):
    def update(self):
        pass

class ActiveView(ActiveObserver):
    def __init__(self, model):
        self._model = model
        self.update()

    def update(self):
        print 'View notified!'
        self._display = 'I have fiery new Active data! Here: {}'.format(self._model.data)

    def __str__(self):
        return self._display

class ActiveModel(object):
    def __init__(self, data_series):
        self._cycle = Cycle(data_series)
        self._observers = []

    def service(self):
        self._cycle.next()
        # An active model is responsible for notifying attached observers.
        self._notify_observers()

    def _notify_observers(self):
        for obs in self._observers:
            obs.update()

    def add_observer(self, observer):
        """
        observer: must have an update method per ActiveObserver
        """
        if not observer:
            raise ValueError('observer cannot be None')
        self._observers.append(observer)

    @property
    def data(self):
        return self._cycle.current

class ActiveController(ActiveObserver):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def update(self):
        print 'Controller notified!'

    def on_event(self):
        self._model.service()
        # The controller does not need to explicitly update the view,
        # since the notification will be sent to model observers.
        # self._view.update()


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

#################################
# Tests
#

def _test_series(expected_data, model, view, controller):
    for index in xrange(0, len(expected_data)):
        print view
        assert str(view).endswith(expected_data[index])
        controller.on_event()

def _test_passive():
    expected_data = 'abcdefghijklmnop'
    model = PassiveModel(expected_data)
    view = PassiveView(model)
    controller = PassiveController(model, view)
    _test_series(expected_data, model, view, controller)
    

def _test_active():
    expected_data = 'abcdefghijklmnop'
    model = ActiveModel(expected_data)
    view = ActiveView(model)
    controller = ActiveController(model, view)
    model.add_observer(view)
    model.add_observer(controller)
    _test_series(expected_data, model, view, controller)


def _test_all():
    _test_passive()
    _test_active()

if __name__ == '__main__':
    _test_all()












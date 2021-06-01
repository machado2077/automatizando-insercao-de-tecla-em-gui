import pytest
from unittest import mock
from process_controller import ProcessController
from mocks import ActuatorMock, ListenerMock, ListenerMockLazy, ListenerMockNone, SensorMock
from response import response


@pytest.fixture
def controller_with_only_the_sensor_mocked():
    sensor = SensorMock()
    listener = ListenerMock()
    sensor._keyboard_listener = listener
    controller = ProcessController(sensor, 'fake_actuator')
    return controller



@pytest.fixture
def controller_with_sensor_and_actuator_mocked():
    listener = ListenerMock()
    sensor = SensorMock()
    sensor._keyboard_listener = listener
    actuator = ActuatorMock()
    return ProcessController(sensor, actuator)



def controller_start_with_no_keyboard_event(controller_with_only_the_sensor_mocked):
    c = controller_with_only_the_sensor_mocked
    c.keyboard_event == response.started



def test_controller_does_not_change_its_keyboard_event_if_listener_is_just_started(controller_with_only_the_sensor_mocked):
    c = controller_with_only_the_sensor_mocked
    c.get_keyboard_event()
    handled_key = c.sensor.handle_keyboard_event_output(response.started)
    assert c.keyboard_event == handled_key



def test_controller_gets_lowercase_initialization_key(controller_with_only_the_sensor_mocked):
    c = controller_with_only_the_sensor_mocked        
    c.sensor._keyboard_listener.key = response.initialize
    c.get_keyboard_event()
    assert c.keyboard_event == response.initialize
    


def test_controller_handles_uppercase_initialization_key(controller_with_only_the_sensor_mocked):
    c = controller_with_only_the_sensor_mocked    
    c.sensor._keyboard_listener.key = response.initialize.upper()
    c.get_keyboard_event()
    assert c.keyboard_event == response.initialize



@mock.patch('mocks.ActuatorMock.respond_to_keyboard_event')
def test_sending_key_event_to_the_actuator_to_initialize(mocked, controller_with_sensor_and_actuator_mocked):
    c = controller_with_sensor_and_actuator_mocked
    c.sensor._keyboard_listener.key = response.initialize
    c.get_keyboard_event()
    c.send_keyboard_event_to_actuator()
    mocked.assert_called_once_with(response.initialize)



@mock.patch('mocks.ActuatorMock.start_key_press')
def test_actuator_method_start_key_press_was_called(mocked, controller_with_sensor_and_actuator_mocked):
    c = controller_with_sensor_and_actuator_mocked
    c.sensor._keyboard_listener.key = response.initialize
    c.get_keyboard_event()
    c.send_keyboard_event_to_actuator()
    mocked.assert_called_once()



@mock.patch('mocks.ActuatorMock.stop_key_press')
def test_actuator_method_stop_key_press_was_called(mocked, controller_with_sensor_and_actuator_mocked):
    c = controller_with_sensor_and_actuator_mocked
    c.sensor._keyboard_listener.key = response.pause.upper()
    c.get_keyboard_event()
    c.send_keyboard_event_to_actuator()
    mocked.assert_called_once()



def test_controller_finishes_processing_keyboard_events(controller_with_sensor_and_actuator_mocked):
    c = controller_with_sensor_and_actuator_mocked
    listener = ListenerMockLazy()
    c.sensor._keyboard_listener = listener
    c.process_keyboard_events()
    assert listener.count == listener.CALL_LIMIT
    assert listener._key == response.finish



def test_no_keyboard_events_provided_are_accepted_by_the_controller(controller_with_sensor_and_actuator_mocked):
    c = controller_with_sensor_and_actuator_mocked
    listener = ListenerMockNone()
    c.sensor._keyboard_listener = listener
    c.process_keyboard_events()
    assert listener.count == listener.CALL_LIMIT
    assert listener._key == response.started
    
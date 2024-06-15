import Python_to_CPP
#---------description
#this file holds the helper functions that'll be used by the API to communicate with the C++ on nova ground
#------------------classes

#the classes might be overkill, so won't use for now
"""
class Device:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        
class Sensor(Device):
    def __init__(self, id, name, units, sensor_type, display_type, read_value_type):
        #init parts from the parent class
        Device.__init__(self, id, name)
        #sensor specific attributes
        self.units = units
        self.sensor_type = sensor_type
        self.display_type = display_type
        self.read_value_type = read_value_type
        
    def read_value():
        return 35; #hardcoded for now, should be taken from C++
        
class Actuator(Device):
    def __init__(self, id, name, actuator_type, current_state_units, current_state_type, list_of_commands):
        #init parts from the parent class
        Device.__init__(self, id, name)
        #sensor specific attributes
        self.actuator_type = actuator_type
        self.current_state_units = current_state_units
        self.current_state_type = current_state_type
        self.list_of_commands = list_of_commands
    
class Motor(Actuator):
    def __init__(self, id, name, actuator_type, current_state_units, current_state_type, list_of_commands):
        Actuator.__init__(self, id, name, actuator_type, current_state_units, current_state_type, list_of_commands)
        
    def get_angle_positoin():
        return 35;#hardcoded for now, should be read from C++
    def set_angle_position(position: float):
        #call talk to the c++
        pass
        
"""
    
#-------dummy data (indexed by their id)
#later on, this will be taken from the C++ stuff
all_devices_dummy_data = [
    {
        "id":"1","name":"servo1","device_type":"actuator",
        "actuator_type":"servo motor",
        "current_state_units":"position in degrees",
        "current_state_type": "float",
        "current_state": "87.5",
        "list_of_commands": [
            {"/servo_position/[position]":"sets the angle position (provided by the float value 'position') of the servo motor in degrees"}
        ]
    },
    {
        "id":"2","name":"thermocouple1","device_type":"sensor",
        "units": "celsius",
        "sensor_type": "thermocouple",
        "display_type": "bar graph",
        "read_value_type": "int",
        "read_value": "67"
    }
]

#-------helper functions
def is_actuator(id:int) -> bool:
    pass
def is_actuator_type(id:int, string:type)->bool:
    pass
    
    
#--------functions
#function to get device properties (as an object) from id 
def get_device(id:int):
    try:
        return all_devices_dummy_data[id]
    except IndexError as e:
        return {
            "Error": "id is not valid"
        }

#function for setting the position of the servo motor
def set_servo_position(id:int, position:float) -> bool:
    #first, check if the specified id is indeed an actuator, and servo motor
    
    is_servo_motor = True #some logic needed for this... using other functions from Nova_Gnd_Interfacing
    #... you check if the device is an actuator and servo motor from the id
    if not is_servo_motor:
        return False
    
    #set the motor to the specified position...
    #write_to_c(id,"set_servo_position", position)
    
    
    #return success
    return True
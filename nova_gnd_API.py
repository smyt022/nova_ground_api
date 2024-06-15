from fastapi import FastAPI
import Nova_Gnd_Interfacing
app = FastAPI()

@app.get('/')
async def root():
    return {
        "message":"welcome to nova gound API",
    }
    
@app.get('/device/read/{id}')
async def read_sensor(id: int):
    #I'm hardcoding example values for now
    #but this will be taken from the c++, with another python script that'll abstract it with get_() functions
    return Nova_Gnd_Interfacing.get_device(id)
    
@app.get('/actuator/write/{id}/servo_position/{position}')
async def write_actuator(id:int, position:float):
    #function will return false, if id doesnt correspond with a servo motor
    success_msg = Nova_Gnd_Interfacing.set_servo_position(id, position)
    if not success_msg:
        return {"error":"ERROR: item with id: "+str(id)+" is not a servo motor"}
    else:
        return {"success":"servo motor with id: "+str(id)+" has been repositioned to: "+str(position)}
    
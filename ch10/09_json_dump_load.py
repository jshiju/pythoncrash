from pathlib import Path
import json

class Car:

    def __init__(self) -> None:
        self.name = 'Maruti'
        self.make = 2023

    def __repr__(self):
        return f"{{name: '{self.name}', make: '{self.make}'}}"

car = Car()
file = Path('car.json')
if file.exists():
    jsonCont = file.read_text()
    print(f'JSON<- {jsonCont}')
else:
    jsonCont = json.dumps(repr(car))
    print(f'JSON-> {jsonCont}')
    file.write_text(jsonCont)
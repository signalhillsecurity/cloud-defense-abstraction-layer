class Technique:
    def __init__(self, technique, cloud, emulation="", detection="") -> None:
        self._technique = technique
        self._cloud = cloud
        self._emulation = ""
        self._detection = ""

    def __repr__(self) -> str:
        return f'Technique(technique="{self._technique}",cloud="{self._cloud}",emulation="{self._emulation}",detection="{self._detection}")'

    ## GETTERS
    @property
    def technique(self):
        return self._technique

    @property 
    def cloud(self):
        return self._cloud 

    @property 
    def emulation(self):
        return self._emulation 

    @property 
    def detection(self):
        return self._detection 

    ## SETTERS
    @technique.setter
    def technique(self, a):
        self._technique = a

    @cloud.setter
    def cloud(self, a):
        allowed_clouds=["AWS","AZURE","GCP","OCI"]
        if a.upper() in allowed_clouds:
            self._cloud = a.upper()
        else:
            raise ValueError(f'{a} is not one of the following allowed clouds: {allowed_clouds}')

    @emulation.setter 
    def emulation(self, a):
        self._emulation = a

    @detection.setter 
    def simulation(self, a):
        self._detection = a

    ## CLASS METHODS
    def json(self) -> str:
        # Return the object in JSON notation
        pass
from datetime import date

class Persona:
    '''Definición de una Persona'''
    
    def __init__(self, nombre=None, fecha_nac=None):
        '''Crea una persona
           Input:
             nombre: Nombre
             fecha_nac: Fecha de  nacimiento en formato ISO
        '''
        self.nombre = nombre
        self.fecha_nacimiento = date.fromisoformat(fecha_nac)
​
    @property
    def edad(self):
        today= date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
    
    @property
    def es_cumple(self):
        today= date.today()
        if self.fecha_nacimiento.month == today.month and self.fecha_nacimiento.day == today.day:
            return True
        else:
            return False
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        if self.es_cumple:
            return f'Yo soy {self.nombre} y hoy cumplo {self.edad} años'
        else:
            return f'Yo soy {self.nombre} y tengo {self.edad} años'
​
class Estudiante(Persona):
    def __init__(self, nombre, fecha_nac, bootcamp='Data Analytics'):
        
        super().__init__(nombre, fecha_nac)
        self.bootcamp = bootcamp
        self.notas = {}
        
    def __str__(self):
        return 'Estudiante de Ironhack'
    
    def __repr__(self):
        return f'{super().__repr__()}. Soy estudiante de {self.bootcamp}'
    
    def hacer_examen(self, asignatura, nota):
        self.notas[asignatura] = nota
        
    @property
    def recuperaciones(self):
        return [ asignatura for asignatura, nota in self.notas.items() if nota < 5]
    
    @property
    def vacaciones(self):
        return not self.recuperaciones
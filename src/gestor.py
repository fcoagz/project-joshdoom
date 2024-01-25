from colorama import Fore
from sqlalchemy.orm import session
from engine import engine 
from models import Estudiante, Representante, Seccion, AnioEscolar, Nota, Grado, Materias, Profesor, Lapso, Evaluacion

def create_profesor(id: int):
        with session(engine) as session:
                for Profesor in session.query(Profesor):
                    if not Profesor.id == id:
                        new_profesor= Profesor(id=id)
                        session.add(new_profesor)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("El profesor ya existe")
                    
def update_profesor(id: int):
        with session(engine) as session:
                try:
                     session.query(Profesor).\
                        filter(Profesor.identification == identification).\
                        update({
                              Profesor.course: course,
                              Profesor.section: section
                        })

                    session.commit()
                except:
                    raise ValueError ("El profesor no existe") 
                           

def create_evaluacion(id: int):
        with session(engine) as session:
                for Profesor in session.query(Evaluacion):
                    if not Evaluacion.id == id:
                        new_evaluacion= Evaluacion(id=id)
                        session.add(new_evaluacion)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La evaluacion esta registrada")

def update_evaluacion(id: int):
        with session(engine) as session:
                try:
                     session.query(Evaluacion).\
                        filter(Evaluacion.identification == identification).\
                        update({
                              Evaluacion.course: course,
                              Evaluacion.section: section
                        })

                    session.commit()
                except:
                    raise ValueError ("La evaluacion no existe")                    

def create_nota(id: int):
        with session(engine) as session:
                for Profesor in session.query(Nota):
                    if not Nota.id == id:
                        new_nota= Nota(id=id)
                        session.add(new_nota)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("La nota es igual")

def update_nota(id: int):
        with session(engine) as session:
                try:
                     session.query(Nota).\
                        filter(Nota.identification == identification).\
                        update({
                              Nota.course: course,
                              Nota.section: section
                        })

                    session.commit()
                except:
                    raise ValueError ("La nota no existe")

def create_lapso(id: int):
        with session(engine) as session:
                for Profesor in session.query(Lapso):
                    if not Lapso.id == id:
                        new_lapso= Lapso(id=id)
                        session.add(new_lapso)
                        session.commit()


                            
                           
                    else:
                          raise ValueError("Lapso ya esta registrado")
                    
def update_lapso(id: int):
        with session(engine) as session:
                try:
                     session.query(Lapso).\
                        filter(Lapso.identification == identification).\
                        update({
                              Lapso.course: course,
                              Lapso.section: section
                        })

                    session.commit()
                except:
                    raise ValueError ("El lapso no existe") 


                    


        
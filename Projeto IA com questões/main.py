from pyke import knowledge_engine, krb_traceback, goal, ask_tty

import sys
import numpy as np

engine = knowledge_engine.engine(__file__)

engine.ask_module = ask_tty


def bc_test():
    engine.reset()      # Allows us to run tests multiple times.
    
    comentarios = []

    print("\nInsira os dados da água que deseja reutilizar\n")
    
    engine.activate('water_reuse_rules')

    with engine.prove_goal(
        'water_reuse_rules.comentarios($comentarios)') as gen:
        for vars, plan in gen:
            comentarios.append(vars['comentarios'])

    print("\nComentários sobre a água que deseja fazer reúso:\n")
    for i in range(len(comentarios)):
        print("-----------------------")
        print(comentarios[i])

bc_test()

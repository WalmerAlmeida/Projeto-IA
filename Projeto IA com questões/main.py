from pyke import knowledge_engine, krb_traceback, goal, ask_tty

import sys

engine = knowledge_engine.engine(__file__)

engine.ask_module = ask_tty


def bc_test():
    engine.reset()      # Allows us to run tests multiple times.
    
    print("\nInsira os dados da água que deseja reutilizar\n")
    
    engine.activate('water_reuse_rules')

    print("doing proof")
    try:
        with engine.prove_goal(
            'water_reuse_rules.qual_classe($classe)') as gen:
            for vars, plan in gen:
                print("A classe da água é: %s" % (vars['classe']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    
    print()
    print("done")
    #engine.print_stats()

bc_test()

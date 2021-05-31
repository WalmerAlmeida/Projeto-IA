from pyke import knowledge_engine, krb_traceback, goal

import sys

engine = knowledge_engine.engine(__file__)


def bc_test():
    engine.reset()      # Allows us to run tests multiple times.
    
    
    engine.activate('water_reuse_rules')
    

    print("doing proof")
    try:
        with engine.prove_goal('water_reuse_rules.qual_classe($classe, $turbidez, $coliformes_termotolerantes, $solidos_dissolvidos_totais, $cloro_residual)', turbidez = 4, coliformes_termotolerantes = 100, solidos_dissolvidos_totais = 100, cloro_residual = 1) as gen:
            for vars, plan in gen:
                print("A classe da água é: %s" % (vars['classe']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    
    print()
    print("done")
    engine.print_stats()

bc_test()
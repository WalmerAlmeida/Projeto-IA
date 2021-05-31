# water_reuse_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def qual_classe_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'pH', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "water_reuse_rules.qual_classe_1: got unexpected plan from when clause 1"
            if context.lookup_data('turbidez') <= 5:
              if context.lookup_data('coliformes_termotolerantes') <= 200:
                if context.lookup_data('solidos_dissolvidos_totais') <= 200:
                  if context.lookup_data('cloro_residual') < 1.5:
                    if context.lookup_data('cloro_residual') > 0.5:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('water_reuse_rules')
  
  bc_rule.bc_rule('qual_classe_1', This_rule_base, 'qual_classe',
                  qual_classe_1, None,
                  (pattern.pattern_literal(1),
                   contexts.variable('turbidez'),
                   contexts.variable('coliformes_termotolerantes'),
                   contexts.variable('solidos_dissolvidos_totais'),
                   contexts.variable('cloro_residual'),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '../water_reuse_rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 26), (7, 7)),
    ((27, 27), (8, 8)),
    ((28, 28), (9, 9)),
    ((29, 29), (10, 10)),
    ((30, 30), (11, 11)),
)

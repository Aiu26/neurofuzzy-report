import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables and membership functions
traffic_flow = ctrl.Antecedent(np.arange(0, 101, 1), 'traffic_flow')
congestion = ctrl.Antecedent(np.arange(0, 101, 1), 'congestion')
light_timing = ctrl.Consequent(np.arange(0, 101, 1), 'light_timing')

traffic_flow['low'] = fuzz.trimf(traffic_flow.universe, [0, 0, 50])
traffic_flow['moderate'] = fuzz.trimf(traffic_flow.universe, [20, 50, 80])
traffic_flow['high'] = fuzz.trimf(traffic_flow.universe, [50, 100, 100])

congestion['low'] = fuzz.trimf(congestion.universe, [0, 0, 50])
congestion['moderate'] = fuzz.trimf(congestion.universe, [20, 50, 80])
congestion['high'] = fuzz.trimf(congestion.universe, [50, 100, 100])

light_timing['short'] = fuzz.trimf(light_timing.universe, [0, 0, 50])
light_timing['medium'] = fuzz.trimf(light_timing.universe, [20, 50, 80])
light_timing['long'] = fuzz.trimf(light_timing.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(traffic_flow['low'] & congestion['low'], light_timing['long'])
rule2 = ctrl.Rule(traffic_flow['low'] & congestion['moderate'], light_timing['medium'])
rule3 = ctrl.Rule(traffic_flow['low'] & congestion['high'], light_timing['short'])
rule4 = ctrl.Rule(traffic_flow['moderate'] & congestion['low'], light_timing['medium'])
rule5 = ctrl.Rule(traffic_flow['moderate'] & congestion['moderate'], light_timing['medium'])
rule6 = ctrl.Rule(traffic_flow['moderate'] & congestion['high'], light_timing['short'])
rule7 = ctrl.Rule(traffic_flow['high'] & congestion['low'], light_timing['short'])
rule8 = ctrl.Rule(traffic_flow['high'] & congestion['moderate'], light_timing['short'])
rule9 = ctrl.Rule(traffic_flow['high'] & congestion['high'], light_timing['short'])

# Define fuzzy control system
traffic_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
traffic_light = ctrl.ControlSystemSimulation(traffic_ctrl)

# Simulate traffic conditions
traffic_flows = [10, 50, 90]
congestions = [10, 50, 90]
for traffic_flow_val in traffic_flows:
    for congestion_val in congestions:
        traffic_light.input['traffic_flow'] = traffic_flow_val
        traffic_light.input['congestion'] = congestion_val
        traffic_light.compute()
        print(f"Traffic Flow: {traffic_flow_val}, Congestion: {congestion_val}, Light Timing: {traffic_light.output['light_timing']}")
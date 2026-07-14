def simulate_dfa(states, alphabet, transitions, start, finals, string):

    current = start

    trace = [current]

    for symbol in string:

        key = (current, symbol)

        if key not in transitions:

            return False, trace

        current = transitions[key]

        trace.append(current)

    return current in finals, trace
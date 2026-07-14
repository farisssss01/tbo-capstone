from flask import Flask, render_template, request

from modules.fsa import simulate_dfa
from modules.graph import draw_dfa
from modules.regex_engine import regex_match
from modules.regex_engine import regex_match, explain_regex
from modules.cfg import (
    validate_cfg,
    parse_cfg,
    tampilkan_cfg,
    leftmost_derivation
)
from modules.tree import draw_parse_tree
from modules.chomsky import classify_grammar, convert_to_cnf
from modules.pda import PDASimulator

app = Flask(__name__)


# ==========================
# HOME
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# FSA
# ==========================

@app.route("/fsa", methods=["GET", "POST"])
def fsa():

    result = None
    trace = None
    table = []

    states = []
    alphabet = []
    start = ""
    finals = []

    if request.method == "POST":

        states = [x.strip() for x in request.form["states"].split(",") if x.strip()]
        alphabet = [x.strip() for x in request.form["alphabet"].split(",") if x.strip()]
        start = request.form["start"].strip()
        finals = [x.strip() for x in request.form["finals"].split(",") if x.strip()]
        string = request.form["string"].strip()

        transitions = {}

        lines = request.form["transitions"].splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            try:

                left, right = line.split("=")
                state, symbol = left.split(",")

                state = state.strip()
                symbol = symbol.strip()
                next_state = right.strip()

                transitions[(state, symbol)] = next_state

                table.append(
                    (
                        state,
                        symbol,
                        next_state
                    )
                )

            except ValueError:
                continue

        result, trace = simulate_dfa(
            states,
            alphabet,
            transitions,
            start,
            finals,
            string
        )

        try:
            draw_dfa(
                transitions,
                finals
            )
        except Exception as e:
            print("Graph Error :", e)

    return render_template(
        "fsa.html",
        result=result,
        trace=trace,
        table=table,
        states=states,
        alphabet=alphabet,
        start=start,
        finals=finals
    )


# ==========================
# REGEX
# ==========================

@app.route("/regex", methods=["GET", "POST"])
def regex():

    result = None

    explanation = []

    pattern = ""

    string = ""

    if request.method == "POST":

        pattern = request.form["pattern"]

        string = request.form["string"]

        result = regex_match(
            pattern,
            string
        )

        explanation = explain_regex(pattern)

    return render_template(

        "regex.html",

        result=result,

        explanation=explanation,

        pattern=pattern,

        string=string

    )


# ==========================
# PDA
# ==========================

@app.route("/pda", methods=["GET", "POST"])
def pda():

    accepted = None

    stack_trace = []

    valid = True

    message = ""

    grammar = ""

    string = ""

    rules = None

    derivation = None

    if request.method == "POST":

        grammar = request.form["grammar"]

        string = request.form["string"]

        valid, message = validate_cfg(grammar)

        if valid:

            cfg = parse_cfg(grammar)

            pda = PDASimulator(cfg)

            accepted = pda.simulate(string)

            stack_trace = pda.get_trace()

            rules = tampilkan_cfg(cfg)

            derivation = leftmost_derivation(
                cfg,
                string
            )

            draw_parse_tree(derivation)

            try:
                draw_parse_tree(derivation)
            except Exception as e:
                print("Tree Error :", e)

        rules = tampilkan_cfg(cfg)

        derivation = leftmost_derivation(
            cfg,
            string
        )
        try:
            draw_parse_tree(derivation)
        except Exception as e:
            print("Tree Error :", e)

    return render_template(

        "pda.html",

        grammar=grammar,

        string=string,

        rules=rules,

        derivation=derivation,
        
        valid=valid,

        message=message,

        accepted=accepted,

        stack_trace=stack_trace,

    )


# ==========================
# CHOMSKY
# ==========================

@app.route("/chomsky", methods=["GET", "POST"])
def chomsky():

    grammar = ""

    grammar_type = None

    reasons = []

    cnf_steps = None

    if request.method == "POST":

        grammar = request.form["grammar"]

        grammar_type, reasons = classify_grammar(grammar)

        cnf_steps = convert_to_cnf(grammar)

    return render_template(

    "chomsky.html",

    grammar=grammar,

    grammar_type=grammar_type,

    reasons=reasons,

    cnf_steps=cnf_steps

)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

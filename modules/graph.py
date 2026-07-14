import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx

def draw_dfa(transitions, finals):

    graph = nx.MultiDiGraph()

    for (state, symbol), next_state in transitions.items():
        graph.add_edge(state, next_state, label=symbol)

    pos = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(8,6))

    colors = []

    for node in graph.nodes():

        if node in finals:
            colors.append("lightgreen")
        else:
            colors.append("skyblue")

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_color=colors,
        node_size=1800
    )

    nx.draw_networkx_labels(graph, pos)

    nx.draw_networkx_edges(
        graph,
        pos,
        arrows=True,
        arrowsize=20
    )

    edge_labels = {}

    for u, v, data in graph.edges(data=True):
        edge_labels[(u, v)] = data["label"]

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels
    )

    os.makedirs("static/img", exist_ok=True)

    plt.axis("off")

    plt.savefig(
        "static/img/dfa.png",
        bbox_inches="tight"
    )

    plt.close()
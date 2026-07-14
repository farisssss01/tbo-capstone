import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
import os


class ParseTree:

    def __init__(self):

        self.graph = nx.DiGraph()
        self.count = 0

    def new_node(self, label):

        node = f"{label}_{self.count}"
        self.count += 1

        self.graph.add_node(node, label=label)

        return node

    def build(self, derivation):

        if not derivation:
            return

        root = self.new_node(derivation[0])

        current = root

        for step in derivation[1:]:

            child = self.new_node(step)

            self.graph.add_edge(current, child)

            current = child

    def save(self):

        os.makedirs("static/img", exist_ok=True)

        plt.figure(figsize=(10, 6))

        pos = nx.spring_layout(self.graph, seed=42)

        labels = nx.get_node_attributes(
            self.graph,
            "label"
        )

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_color="lightblue",
            node_size=2200
        )

        nx.draw_networkx_edges(
            self.graph,
            pos,
            arrows=True
        )

        nx.draw_networkx_labels(
            self.graph,
            pos,
            labels
        )

        plt.axis("off")

        plt.savefig(
            "static/img/parse_tree.png",
            bbox_inches="tight"
        )

        plt.close()


def draw_parse_tree(derivation):

    tree = ParseTree()

    tree.build(derivation)

    tree.save()
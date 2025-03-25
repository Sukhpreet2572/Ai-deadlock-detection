import networkx as nx

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_graph_from_table(self, table_data):
        """Build graph from table data"""
        self.graph = nx.DiGraph()
        processes = ["P1", "P2", "P3", "P4", "P5"]
        
        for i in range(5):
            for j in range(5):
                if table_data[i][j] == "1":
                    self.graph.add_edge(processes[i], processes[j])
        
        return self.graph
    
    def detect_deadlock(self):
        """Detect and classify deadlock type"""
        if not self.graph or not self.graph.edges:
            return "No Deadlock"

        edges = list(self.graph.edges)
        edges_set = set(edges)

        # Check for self-loops
        if any(u == v for u, v in edges):
            return "🔴 Mutual Exclusion Deadlock (Self-loop detected)."

        # Check for bidirectional edges
        if any((v, u) in edges_set for u, v in edges):
            try:
                nx.find_cycle(self.graph, orientation="original")
                return "🟠 Circular Wait Deadlock (Processes waiting in a cycle)."
            except nx.NetworkXNoCycle:
                return "🟡 No Preemption Deadlock (Irreversible resource holding)."

        # Check for cycles
        try:
            nx.find_cycle(self.graph, orientation="original")
            return "🟠 Circular Wait Deadlock (Processes waiting in a cycle)."
        except nx.NetworkXNoCycle:
            pass

        # Check for Hold and Wait
        for u in self.graph.nodes:
            outgoing = set(v for _, v in self.graph.out_edges(u))
            incoming = set(v for v, _ in self.graph.in_edges(u))
            if outgoing and incoming and u not in outgoing:
                return "🔵 Hold and Wait Deadlock (Processes holding resources and waiting)."

        return "No Deadlock"

    def resolve_deadlock(self):
        """Attempt to resolve deadlock by breaking cycle"""
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            process_to_remove = cycle[0][0]
            self.graph.remove_node(process_to_remove)
            return process_to_remove
        except nx.NetworkXNoCycle:
            return None

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Graph Visualizer")
st.write("Enter vertices and edges to visualize the graph.")

# Input for vertices
vertex_input = st.text_input("Vertices (comma-separated)", "A,B,C,D")

# Input for edges
edge_input = st.text_input("Edges (format: A-B,B-C,C-D)", "A-B,B-C,C-A,C-D")

# Button to build the graph
if st.button("Build Graph"):
    vertices = [v.strip() for v in vertex_input.split(",")]
    edges_raw = [e.strip() for e in edge_input.split(",")]
    edges = [(u.strip(), v.strip()) for e in edges_raw if "-" in e for u, v in [e.split("-")]]

    # Create the graph
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)

    # Show info about each vertex
    st.subheader("Vertex Information:")
    for v in G.nodes():
        st.write(f"Vertex {v}: degree = {G.degree[v]}, neighbors = {list(G.neighbors(v))}")

    # Draw the graph
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=14, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}-{v}" for u, v in G.edges()}, ax=ax)
    plt.title("Graph")
    st.pyplot(fig)
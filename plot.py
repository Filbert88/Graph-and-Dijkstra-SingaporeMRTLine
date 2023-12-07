import networkx as nx
import plotly.graph_objects as go
from graph import *

def plot_graph(shortest_path_edges):
    G = nx.Graph()

    for stations, times in zip([blue_stations, purple_stations, green_stations, red_stations, circle_stations, thomson_stations], [blue_times, purple_times, green_times, red_times, circle_times, thomson_times]):
        for i in range(len(stations) - 1):
            G.add_edge(stations[i], stations[i + 1], weight=times[i])

    pos = nx.kamada_kawai_layout(G)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), mode='lines')
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=text, textposition='top center',
                            marker=dict(showscale=False, color='#888', size=5), hoverinfo='text')


    shortest_path_edge_x = []
    shortest_path_edge_y = []
    for i in range(len(shortest_path_edges) - 1):
        x0, y0 = pos[shortest_path_edges[i]]
        x1, y1 = pos[shortest_path_edges[i + 1]]
        shortest_path_edge_x.extend([x0, x1, None])
        shortest_path_edge_y.extend([y0, y1, None])

    shortest_path_trace = go.Scatter(x=shortest_path_edge_x, y=shortest_path_edge_y, line=dict(width=2, color='red'), mode='lines')

    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace, shortest_path_trace],
                    layout=go.Layout(
                        title='<br>Network graph of Singapore MRT',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code with NetworkX and Plotly",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.add_trace(shortest_path_trace)
    fig.update_layout(showlegend=False)

    fig.show()

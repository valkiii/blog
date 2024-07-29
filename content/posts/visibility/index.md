---
title: My heart beats like a network
subtitle: 

# Summary for listings and search engines
summary: I was looking for a way to automate the process behind updating my site, and I found one.

# Link this post with a project
projects: []

# Date published
date: "2024-07-11T00:00:00Z"

# Date updated
lastmod: "2024-07-11T00:00:00Z"

# Is this an unpublished draft?
draft: true

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 'Image credit: DALL-E'
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- admin

tags:
- Optimization
- Bash
- Coding

categories:
- Coding
- Optimization
---

# 

---
![alt text](featured.png)

In the realm of data science, researchers and practitioners are constantly seeking innovative approaches to extract meaningful insights from complex datasets. One such approach that has gained significant attention in recent years is the concept of visibility graphs [1]. In this blog post, we will delve into the fundamentals of visibility graphs, explore their mathematical underpinnings, and showcase their potential applications in various domains.


### Understanding Visibility Graphs through Skyscrapers

In data visualization and analysis, a visibility graph is a powerful tool for representing relationships between data points. However, the concept can sometimes be abstract and challenging to grasp. To make this easier to understand, let's use a more tangible metaphor: skyscrapers in a bustling city.

Picture yourself in a city filled with towering skyscrapers, each representing a point in time or a specific data value. The height of each skyscraper corresponds to the magnitude of the data point it represents. These skyscrapers are arranged in a line along a single street, much like data points along a time series.

![alt text](cityscape.png)


Now, imagine you are standing on the roof of one of these skyscrapers. From your vantage point, you can see some buildings down the line, while others are obscured by taller structures in between. This scenario is a perfect analogy for understanding visibility graphs.

### The Concept of Visibility
In our metaphor, visibility means whether you can see the roof of one skyscraper from the roof of another. For two skyscrapers to see each other (i.e., to have a line of sight), there must be no other skyscraper in between that is as tall or taller. This is analogous to checking if one data point can "see" another without being obscured by an intermediate point.

<mark> Direct Line of Sight</mark>: If skyscraper A is 50 meters tall and skyscraper B, further down the street, is 100 meters tall, you can see B from A if no other skyscraper in between is taller than 50 meters at the point it blocks the line of sight.

Blocked Visibility: If there's a skyscraper C that is 120 meters tall between A and B, then A cannot see B. This blockage happens because C's height interferes with the direct line of sight from A to B.

Building the Visibility Graph
To construct a visibility graph from this setup:

Nodes: Each node represents a skyscraper. The horizontal position of a node corresponds to the position of the skyscraper on the street, and the vertical position represents its height.

Edges: An edge between two nodes indicates a clear line of sight between the corresponding skyscrapers. If skyscraper A can see skyscraper B, an edge is drawn between the nodes representing these two skyscrapers.

Visualizing the Concept with Code
In the provided Python code:

Random Heights Generation: Heights for 15 skyscrapers are generated randomly, simulating the varying data points in a dataset.
Visibility Calculation: The code checks each pair of skyscrapers to determine if there's a direct line of sight between them, considering potential obstructions by other skyscrapers in between. If there is no obstruction, an edge is created in the visibility graph.
The resulting visualization consists of two main parts:

- Time Series (Bar Chart): This shows the heights of the skyscrapers over a sequence, with visibility lines overlaid to illustrate which skyscrapers can see each other.

- Visibility Graph Network (Scatter Plot): This plot displays the nodes and edges, representing the skyscrapers and their visibility relationships, respectively. The nodes are placed according to their sequence and heights, while the edges represent the lines of sight.

### Why Use Visibility Graphs?
This visualization technique is particularly useful in analyzing time series data, where understanding the relationships and dependencies between different data points is crucial. For instance, in financial data analysis, a visibility graph can help identify periods where market behaviors are similar or influenced by similar factors, despite potential intervening data points.

By using the metaphor of skyscrapers, we can simplify the concept of visibility graphs, making it more accessible and easier to understand. This approach not only helps in visualizing the data but also in drawing insights from complex datasets.

In summary, the visibility graph and skyscraper metaphor provide a unique and intuitive way to explore and understand the relationships within data, helping us see the bigger picture without losing sight of the details.

At its core, a visibility graph is a representation of a time series or a spatial dataset where each data point is treated as a node, and an edge is created between two nodes if they have a clear line of sight. Formally, given a time series {x_i}_(i=1)^N, a visibility graph is constructed by connecting nodes i and j if and only if [2]:

x_i, x_j > x_n for all n such that i < n < j

This formulation ensures that two nodes are connected if no intermediate data point obscures their visibility. The resulting graph encodes the structural properties of the original dataset, revealing patterns, and relationships that may not be immediately apparent.

The construction of visibility graphs relies on the visibility algorithm, which efficiently computes the edges between nodes. The algorithm has a time complexity of O(N^2), where N is the number of data points. However, recent advancements have led to the development of more efficient algorithms, such as the horizontal visibility graph algorithm, which reduces the time complexity to O(N log N) [3].

One of the key advantages of visibility graphs lies in their ability to capture both local and global properties of the dataset. Local properties, such as the degree distribution of nodes, provide insights into the immediate neighborhood of each data point. On the other hand, global properties, such as the average path length and clustering coefficient, reveal the overall structure and connectivity of the graph [4].

From a mathematical perspective, visibility graphs exhibit intriguing properties that have been extensively studied. For instance, the degree distribution of visibility graphs constructed from fractal time series follows a power law, P(k) ~ k^(-γ), where k is the degree and γ is the scaling exponent [5]. This property has been leveraged to characterize the complexity and self-similarity of time series data.


To better understand how visibility graphs work, interact with the demonstration below. This visualization shows how a simple time series is transformed into a visibility graph, highlighting the connections between data points based on their visibility.

<iframe src="/interactive_visibility_graph.html" width="100%" height="850" frameborder="0"></iframe>


Moreover, visibility graphs have found applications in various domains, ranging from finance to neuroscience. In finance, visibility graphs have been used to analyze stock market dynamics, detect market inefficiencies, and predict future price movements [6]. By constructing visibility graphs from stock price time series, researchers have uncovered hidden patterns and correlations that traditional methods may overlook.

In neuroscience, visibility graphs have been employed to study the complex dynamics of brain activity. By transforming brain signals, such as EEG or fMRI data, into visibility graphs, researchers can characterize the functional connectivity and synchronization of different brain regions [7]. This approach has shed light on the intricate workings of the brain and has potential implications for understanding neurological disorders.

As the field of data science continues to evolve, visibility graphs remain a powerful tool in the arsenal of researchers and practitioners. Their ability to uncover hidden patterns, quantify complex dynamics, and provide a fresh perspective on data analysis makes them an invaluable asset. With ongoing research and development, we can expect to see further advancements in the theory and applications of visibility graphs, pushing the boundaries of what is possible in data science.

In conclusion, visibility graphs offer a unique and compelling approach to data analysis, bridging the gap between time series, spatial data, and network science. By leveraging their mathematical properties and algorithmic efficiency, data scientists can gain deeper insights, make more accurate predictions, and unlock the full potential of their datasets. As we continue to explore the power of visibility graphs, we can look forward to a future where data-driven decision-making is more precise, efficient, and impactful than ever before.

<iframe src="/heart_rate_visibility_graph_communities.html" width="100%" height="820" frameborder="0"></iframe>


The final network:

<iframe src="/final_network_snapshot_interactive.html" width="100%" height="450" frameborder="0"></iframe>

-------

## References

[1] Lacasa, L., Luque, B., Ballesteros, F., Luque, J., & Nuno, J. C. (2008). From time series to complex networks: The visibility graph. Proceedings of the National Academy of Sciences, 105(13), 4972-4975.

[2] Luque, B., Lacasa, L., Ballesteros, F., & Luque, J. (2009). Horizontal visibility graphs: Exact results for random time series. Physical Review E, 80(4), 046103.

[3] Lan, X., Mo, H., Chen, S., Liu, Q., & Deng, Y. (2015). Fast transformation from time series to visibility graphs. Chaos: An Interdisciplinary Journal of Nonlinear Science, 25(8), 083105.

[4] Ahmadlou, M., Adeli, H., & Adeli, A. (2010). New diagnostic EEG markers of the Alzheimer's disease using visibility graph. Journal of Neural Transmission, 117(9), 1099-1109.

[5] Lacasa, L., & Toral, R. (2010). Description of stochastic and chaotic series using visibility graphs. Physical Review E, 82(3), 036120.

[6] Yang, Y., Wang, J., Yang, H., & Mang, J. (2009). Visibility graph approach to exchange rate series. Physica A: Statistical Mechanics and its Applications, 388(20), 4431-4437.

[7] Ahmadlou, M., Ahmadi, K., Rezazade, M., & Azad-Marzabadi, E. (2013). Global organization of functional brain connectivity in methamphetamine abusers. Clinical Neurophysiology, 124(6), 1122-1131.
---
title: "Degree correlations in signed social networks"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- et al.

# Author notes (optional)
#author_notes:
#- "Equal contribution"

date: "2021-11-19T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2015-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
# publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Physica A*
publication_short: In *Physica A*

abstract: We investigate degree correlations in two online social networks where users are connected through different types of links. We find that, while subnetworks in which links have a positive connotation, such as endorsement and trust, are characterized by assortative mixing by degree, networks in which links have a negative connotation, such as disapproval and distrust, are characterized by disassortative patterns. We introduce a class of simple theoretical models to analyze the interplay between network topology and the superimposed structure based on the sign of links. Results uncover the conditions that underpin the emergence of the patterns observed in the data, namely the assortativity of positive subnetworks and the disassortativity of negative ones. We discuss the implications of our study for the analysis of signed complex networks.

# Summary. An optional shortened abstract.
summary: We investigate degree correlations in two online social networks where users are connected through different types of links. We find that, while subnetworks in which links have a positive connotation, such as endorsement and trust, are characterized by assortative mixing by degree, networks in which links have a negative connotation, such as disapproval and distrust, are characterized by disassortative patterns. We introduce a class of simple theoretical models to analyze the interplay between network topology and the superimposed structure based on the sign of links. Results uncover the conditions that underpin the emergence of the patterns observed in the data, namely the assortativity of positive subnetworks and the disassortativity of negative ones. We discuss the implications of our study for the analysis of signed complex networks.


tags: [Network Analysis, Sentiment Analysis, Complex Network, Signed Networks]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://www.sciencedirect.com/science/article/abs/pii/S0378437114010334'
#url_code: ''
#url_dataset: ''
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: ''
#url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Example of signed network'
  focal_point: "Smart"
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

<p align="center">
  <img src="featured.png" alt="alt text">
</p>

As a researcher in network science, I recently embarked on a fascinating journey to explore the intricate world of signed social networks. My goal was to uncover hidden patterns that emerge when we consider both positive and negative relationships in online communities.

Social networks are typically studied as purely positive structures, where connections represent friendships or collaborations. However, real-world social interactions are far more nuanced, including both positive and negative relationships. I wanted to investigate how the sign of these relationships affects the network's structural properties, particularly focusing on degree correlations - the tendency of nodes to connect with others of similar degree.

To tackle this problem, I analyzed two online social networks: Epinions, a product review site where users can trust or distrust each other, and Slashdot, a technology news site where users can mark others as friends or foes. Both networks contained hundreds of thousands of users and relationships, with a mix of positive and negative connections.

My methodology involved separating each network into positive and negative subnetworks and analyzing their degree distributions and correlations. To better understand the underlying mechanisms, I developed a class of models to simulate signed networks with various properties. These models allowed me to explore random networks with binomial degree distributions, scale-free networks with power-law degree distributions, and networks split into two or more mutually exclusive groups. By varying conditions such as structural balance, group sizes, and the assortativity of the unsigned network, I could compare the degree correlations in the simulated positive and negative subnetworks under different scenarios.

The results were intriguing. In both real-world networks, the positive subnetworks showed assortative mixing, where nodes of similar degree tend to connect. In contrast, the negative subnetworks exhibited disassortative mixing, with nodes of dissimilar degree tending to connect. Our models revealed that this pattern emerges under specific conditions: when the unsigned network is assortative or uncorrelated, the signed network is structurally balanced, and nodes are unevenly allocated into groups. Under these conditions, the positive subnetwork remains assortative, while the negative subnetwork becomes disassortative, regardless of the unsigned network's pattern.

<div class="quote-container">
  <blockquote class="styled-quote">
    <div class="quote-rectangle"></div>
    <p>"The sign of social relationships is not just a detail - it's a key that unlocks hidden structural patterns in networks."</p>
  </blockquote>
  <p>These findings challenge the notion that community structure alone explains assortative mixing in social networks. Instead, the nature and sign of the relationships appear to be key factors in determining network structure. The widely observed assortativity in social networks may be primarily due to positive relationships, while negative relationships exhibit different patterns. This research opens up several exciting avenues for future exploration. </p>
</div>

We could develop methods to infer the sign of links based on observed mixing patterns, investigate degree correlations across subnetworks, extend the model to account for more complex relationship types and multiplex networks, and apply these insights to better understand and predict dynamics in online communities and organizational networks.

By considering the sign of relationships, we can uncover hidden structural properties in social networks that would otherwise remain concealed. This approach promises to enhance our understanding of complex social systems and could lead to more accurate models and predictions in various domains, from online community management to organizational behavior. As we continue to explore the nuances of signed networks, we're likely to gain even deeper insights into the complex tapestry of human social interactions in the digital age.

<style>
.quote-container {
  margin: 1em 0;
  overflow: hidden;
  width: 100%; /* Ensure container doesn't exceed body width */
}

.styled-quote {
  /* background-color: #f9f9f9; */
  padding: 1em 0.8em 0.8em 0; /* Removed left padding */
  position: relative;
  margin: 0 0 1em 0;
  border: none;
  font-size: 1.2em;
}

.styled-quote p {
  margin: 0;
  padding-left: 15px; /* Should match the width of the rectangle */
  font-style: italic;
  text-decoration: underline;
  text-decoration-color: #ccc;
  text-underline-offset: 3px;
}

.quote-rectangle {
  width: 30px;
  height: 15px;
  background-color: #4CAF50;
  position: absolute;
  top: 0;
  left: 0;
}

.quote-container > p {
  font-size: 1em;
  margin: 0;
  overflow: hidden; /* Prevent text overflow */
}

@media (min-width: 768px) {
  .quote-container {
    position: relative;
    left: -5%;
    width: 105%; /* Slightly less overflow */
  }

  .styled-quote {
    float: left;
    width: 35%; /* Smaller width for the quote box */
    margin-right: -1em;
    margin-bottom: 0.5em;
  }
  
  .quote-container > p {
    width: calc(65% - 1em); /* Adjust width to prevent overflow */
    float: right;
  }
}

@media (max-width: 767px) {
  .quote-container {
    width: 100%;
    margin-left: 0;
  }

  .styled-quote {
    width: 100%;
  }
}
</style>

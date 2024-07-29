---
title: "Predicting success in the worldwide start-up network"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Moreno Bonaventura
- et al.

# Author notes (optional)
author_notes:
- "Equal contribution"
- "Equal contribution"

date: "2020-01-15T00:00:00Z"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-01-15T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
# publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: In *Nature Scientific Reports*
publication_short: In *Nature Scientific Reports*

abstract: By drawing on large-scale online data we are able to construct and analyze the time-varying worldwide network of professional relationships among start-ups. The nodes of this network represent companies, while the links model the flow of employees and the associated transfer of know-how across companies. We use network centrality measures to assess, at an early stage, the likelihood of the long-term positive economic performance of a start-up. We find that the start-up network has predictive power and that by using network centrality we can provide valuable recommendations, sometimes doubling the current state of the art performance of venture capital funds. Our network-based approach supports the theory that the position of a start-up within its ecosystem is relevant for its future success, while at the same time it offers an effective complement to the labour-intensive screening processes of venture capital firms. Our results can also enable policy-makers and entrepreneurs to conduct a more objective assessment of the long-term potentials of innovation ecosystems, and to target their interventions accordingly.

# Summary. An optional shortened abstract.
summary: By drawing on large-scale online data we are able to construct and analyze the time-varying worldwide network of professional relationships among start-ups. The nodes of this network represent companies, while the links model the flow of employees and the associated transfer of know-how across companies. We use network centrality measures to assess, at an early stage, the likelihood of the long-term positive economic performance of a start-up. We find that the start-up network has predictive power and that by using network centrality we can provide valuable recommendations, sometimes doubling the current state of the art performance of venture capital funds. Our network-based approach supports the theory that the position of a start-up within its ecosystem is relevant for its future success, while at the same time it offers an effective complement to the labour-intensive screening processes of venture capital firms. Our results can also enable policy-makers and entrepreneurs to conduct a more objective assessment of the long-term potentials of innovation ecosystems, and to target their interventions accordingly.


tags: [Network Analysis, Success, Complex Network, Startups, Unicorn]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://www.nature.com/articles/s41598-019-57209-w'
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
  caption: 
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

![alt text](featured.png)


Our study explores the intricate world of start-ups by constructing and analyzing a global network of professional relationships. This network, which we call the <mark> Worldwide Startup (WWS) network </mark>, encompasses the interactions among companies, driven by the movement of individuals—such as employees, advisors, and investors—across these firms. Our primary aim is to leverage network centrality measures to predict the long-term economic success of start-ups. By focusing on how the position of a start-up within this network can influence its future, we provide a data-driven method that complements the traditional, often subjective, evaluations used by venture capitalists.

### Data Used

Our analysis is based in the dataset from Crunchbase, spanning from 1990 to 2015. This data includes detailed records of companies and the professional roles of individuals associated with them. We constructed a bipartite graph connecting people to start-ups based on these roles, which we then projected into a time-varying, one-mode network of start-ups. This network consists of 41,830 companies and 135,099 links, covering 117 countries. The network is dynamic, reflecting changes over time as companies and individuals interact and evolve.

### Methodology

Our methodological framework involves several key steps. Initially, we built the WWS network by mapping connections based on shared individuals between companies. These connections, represented as edges in our graph, do not vanish over time, signifying the persistent value of know-how and relationships. We then employed centrality measures, such as closeness centrality, to rank start-ups based on their positions within the network. 

<div class="quote-container">
  <blockquote class="styled-quote">
    <div class="quote-rectangle"></div>
    <p>"Companies with higher centrality early on are more likely to experience positive long-term outcomes."</p>
  </blockquote>
  <p>
  This ranking allowed us to hypothesize that companies with higher centrality early on are more likely to experience positive long-term outcomes, such as securing funding, acquisitions, or going public.

  To validate our hypothesis, we focused on a subset of companies—those categorized as "open deals" (firms yet to receive significant financial milestones like funding rounds or IPOs). We assessed the success rate of 
  </p>
</div>
our centrality-based recommendations by tracking these companies' outcomes over a subsequent number of year period in achieving any of the forms of success.
  
  ### Results

The analysis revealed that our network-based approach significantly outperforms random expectations. Specifically, the success rate of start-ups within the top centrality ranks was consistently higher than what would be expected by chance. For instance, in June 2003, our method identified successful companies with a 50% accuracy rate, which is substantially better than the average venture capital success rate of 10-15% for early-stage investments. Our findings suggest that centrality in the WWS network is a strong predictor of future economic performance, offering a valuable tool for investors and policy-makers.

### Future Works

Looking forward, there are several avenues for expanding this research. One critical area is exploring the impact of external factors, such as economic cycles or regional market conditions, on the predictive power of our model. Additionally, refining our centrality measures and incorporating other network features, like community structures or network dynamics over shorter time intervals, could enhance the accuracy of our predictions. Finally, extending the dataset beyond 2015 would help validate the robustness of our findings in more recent contexts, further establishing the WWS network as a reliable framework for assessing start-up potential globally.


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

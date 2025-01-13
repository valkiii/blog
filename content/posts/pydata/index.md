---
title: Hunting unicorns with Network analysis
subtitle: PyData 2024 - Amsterdam

# Summary for listings and search engines
summary: 
# Link this post with a project
projects: []

# Date published
date: "2024-09-14T00:00:00Z"

# Date updated
lastmod: "2024-09-14T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption:  
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- admin

tags:
- Talk
- Startup Network
- Network Analysis

categories:
- Presentation
- Network Analysis


---

<!-- Load KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.css">

<!-- Load KaTeX JavaScript -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/contrib/auto-render.min.js"></script>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "\\[", right: "\\]", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\(", right: "\\)", display: false}
      ]
    });
  });
</script>

<!-- ![alt text](featured.png) -->

<p align="center">
  <img src="presentation.jpg" alt="alt text" width="500", height="350">
</p>

If you were not one of the lucky people to participate at PyData 2024, no worries—you can find my talk on YouTube (see below).

{{< youtube tvSWHWG3iCY >}}


The talk is about the construction and analysis of a time-varying worldwide network of professional relationships among startups to predict long-term economic performance using network centrality measures. In my PyData talk, I provided an overview of how I built the worldwide startup network using CrunchBase data and the Networkx library. I modeled employee flow and knowledge transfer as links between startups. By applying network centrality measures, I ranked early-stage startups (pre-seeded) and evaluated how their ranked positions correlated with their future success. I also touched on the implications of these findings for entrepreneurs, investors, and policymakers.

Drawing on large-scale online data, I modeled professional relationships and employee transitions among startup companies in a time-varying global network. In this network, companies were represented as nodes, while links indicated employee flows and the transfer of knowledge across firms.

I investigated whether a startup’s position and connectivity patterns within this network could predict its long-term economic performance and likelihood of success. Using network centrality measures like PageRank, I ranked startups within the global startup network. My analysis showed that this network provided valuable predictive signals, enabling results that sometimes doubled the performance of traditional venture capital screening processes. These findings supported the idea that a startup’s position within its ecosystem plays a critical role in determining future success.

In the talk, I covered the methodology for network construction, the predictive modeling approach, key findings, and their implications. Entrepreneurs could learn how to optimize their startups’ ecosystem positioning, while venture capitalists and policymakers gained insights into conducting more objective assessments and designing targeted interventions within innovation ecosystems.

This PyData talk was designed for data scientists, network scientists, investors, entrepreneurs, and anyone curious about combining network science and machine learning for empirical studies. I balanced technical modeling details with higher-level insights. A basic understanding of networks/graphs and machine learning concepts would have been helpful, but a strong curiosity about innovative approaches in venture capital made the talk engaging for a wide audience.

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
.centered-figure {
  text-align: center;
}

.centered-figure img {
  display: block;
  margin: 0 auto;
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

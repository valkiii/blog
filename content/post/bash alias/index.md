---
title: Bash functions
subtitle: or how to automate your website updates

# Summary for listings and search engines
summary: I was looking to find a way to automate the process behind updating my site, and I found one.

# Link this post with a project
projects: []

# Date published
date: "2023-01-28T00:00:00Z"

# Date updated
lastmod: "22023-01-28T00:00:00Z"

# Is this an unpublished draft?
draft: false

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

I am grateful that Hugo and Github (and their communit of developers) exist, otherwise I would not have been able to create this website in the first place. However, if you do not spend too much time digging into how everything works, you may end up feeling lost.

I always had a hard time figuring out all the different steps to modify my website locally, push the changes on my repo, and then see them appear (magically) on my github page. To be honest, ~~spending~~ investing a bit of time understanding how all parts interact with one another is not that difficult but, let's be honest, I always first dirty my hands until I can't take it anymore, and finally end up reading about how things are built and meant to work. Note for myself, <mark>investing time studying, it's always the right starting point</mark>.

I think I finally found a way to help myself automating the process of updating my blog (and hopefully keep writing on it more than before). 

---
## How I structured the web site

To keep things easy, I have now two repos:
- one where I develop locally my website using the theme from wowchemy, which goes under the name `blog`.
- one that has the website name `valkiii.github.io` and where I transfer the `public` content of the `blog` repo.


---

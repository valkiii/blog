---
title: Automating Your Website Updates with Hugo and GitHub Pages
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
I am grateful that Hugo and GitHub (and their community of developers) exist; otherwise, I would not have been able to create this website in the first place. However, if you do not spend enough time digging into how everything works, you may end up feeling lost.

I always had a hard time figuring out all the different steps to modify my website locally, push the changes to my repository, and then see them appear (magically) on my GitHub Pages site. To be honest, investing a bit of time understanding how all parts interact with one another is not that difficult. But let's be honest, I always dirty my hands first until I can't take it anymore and finally end up reading about how things are built and meant to work. Note to self: <mark>investing time studying is always the right starting point</mark>.

I think I finally found a way to help myself by automating the process of updating my blog (and hopefully keep writing on it more than before) using a single Bash function.

---
## How I structured the web site

To keep things easy, I have now two repos:
- One where I develop my website locally using the theme from Wowchemy, which goes under the name `blog`.
- One that has the website name `valkiii.github.io` and where I transfer the `public` content of the `blog` repo.
---

I decided that I wanted a simple command to run all this. To do so, I wrote a simple Bash function in my `.bashrc` file containing the following:

![alt text](bash_update.svg)


Let's break down what this function does: First it launches `hugo` to build the website, generating the static files in the public directory. Then I run `rsync -a public/* ../valkiii.github.io/.` to sync the contents of the public directory to the root of my GitHub Pages repository (`valkiii.github.io` in this example). I added the `-a` flag to ensure that all files and directories are copied recursively while preserving permissions and other attributes.

<div class="quote-container">
  <blockquote class="styled-quote">
    <div class="quote-rectangle"></div>
    <p>"Investing time studying is always the right starting point"</p>
  </blockquote>
  <p>Then it's time to add all changes in the current directory (my Hugo project directory) for committing with <code>git add --all</code>. There is not a <code>git add</code> without a following <code>git commit -m "$1"</code> with the only exception that the message that we add the commit get provided as the first argument to the function (<code>$1</code>).
</p>
</div>

These two commands are naturally followed by a <code>git push</code> that pushes the changes to the remote repository, updating the Hugo project repository.

Then I want to actually update my repository on github, to be sure that the day my computer dies, I am still able to continue updating this website. To do so, fI first go back to my repo folder with `cd ../valkiii.github.io`, then, like before, I git add, commit, and push all changes with `git add --all`, `git commit -m "$1"` and `git push`. Finally, I go back to the blog folder to continue modifying and rendering my website locally with `cd ../blog/`.

To use this function, save it in your `.bashrc` or `.bash_profile` file and source the file using source `~/.bashrc` to make the function available in your terminal session. Then, you can simply run update_website "Your commit message" whenever you want to build and deploy your website with a single command.

Note that this script assumes that your blog and `valkiii.github.io` repositories are in the same parent directory.

By automating the build and deployment process with a Bash function, you can save time and ensure consistency in your website updates. Give it a try and adapt it to fit your own website setup!

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

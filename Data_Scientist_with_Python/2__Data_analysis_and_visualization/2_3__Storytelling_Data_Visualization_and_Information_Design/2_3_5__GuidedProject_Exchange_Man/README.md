# Introduction

<div><p>At the beginning of this course, we learned that there are two types of data visualization:</p>
<ul>
<li>Exploratory data visualization: we create graphs for <em>ourselves</em> to better understand and explore data.</li>
<li>Explanatory data visualization: we create graphs for <em>others</em> to inform, make a point, or tell a story.</li>
</ul>
<p>Throughout the course, we focused on explanatory data visualization and learned the following:</p>
<ul>
<li>How to use information design principles (familiarity and maximizing the data-ink ratio) to create better graphs for an audience.</li>
<li>About the elements of a story and how to create storytelling data visualizations using Matplotlib.</li>
<li>How to create visual patterns using Gestalt principles.</li>
<li>How to guide the audience's attention with pre-attentive attributes.</li>
<li>How to use Matplotlib built-in styles — with a case study on the FiveThirtyEight style.</li>
</ul>
<p>To make learning more efficient, we learned about each of these topics one at a time. In this guided project, we'll go one step further and combine these skills.</p>
<p>The dataset we'll use describes Euro daily exchange rates between 1999 and 2021. The euro (symbolized with €) is the official currency in most of the countries of the European Union.</p>
<p>If the exchange rate of the euro to the US dollar is 1.5, you get 1.5 US dollars if you pay 1.0 euro (one euro has more value than one US dollar at this exchange rate). </p>
<p>Daria Chemkaeva put together the data set and made it available on <a href="https://www.kaggle.com/lsind18/euro-exchange-daily-rates-19992020" target="_blank">Kaggle</a> — the data source is the European Central Bank. Note that the dataset gets regular updates — we downloaded it on January 2021.</p>
<p>Let's start by reading in the dataset. While we do this, start thinking about what data visualizations you might want to build using this data. You can find the solution notebook for this project <a href="https://github.com/dataquestio/solutions/blob/master/Mission529Solutions.ipynb" target="_blank">here</a>.</p></div>

### Instructions 

<ol>
<li>Read in the <code>euro-daily-hist_1999_2020.csv</code> file into a pandas <code>DataFrame</code> — store the file into a variable named <code>exchange_rates</code>.</li>
<li>Inspect the first and the last five rows to understand the structure of the dataset.</li>
<li>Use the <code>DataFrame.info()</code> method to learn some basic facts about the dataset:<ul>
<li>What is the number of rows and columns?</li>
<li>Are there null values?</li>
<li>What is the data type of each column?</li>
</ul>
</li>
</ol>

# 
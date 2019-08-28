## NLP Course Homework :project 1

### 一、 extract role and views
#### 1. extract key entity
 - use NER of ltp to find key entity .
 - for example: 雷先生、律师、骆裕德
 
#### 2. extract key views
 - use dependency parsing of ltp to find somebody's key views.
 - for example: 昨日,雷先生说,<u>交警部门...</u>   

#### 3. extract key similar words
 - use wiki or other news corpus to train word2vec, then combine search tree and dynamic programming to find similar words with "说".   
 - for example: 说,讲,...
 
#### 4. confirm the end of sentence
 - easy method is to meet with period, but sometimes step over one more.
 - compare similarity of tf-idf vectorized sentences.
 - weighted word vector and PCA for dimensionality reduction. Refer to  https://openreview.net/pdf?id=SyK00v5xx.
 
### 二、 sentiment classification 
 - according to sentiment division, we can plot a viewpoint's doughnut and list some typical persons for every viewpoint.
  
### 三、 visualize project result
 - a web demo contains these functions,such as show everyone's view when you input a news and chart display about everyone's sentiment 
 - related technology: Flask/Bottle(back-end framework),Bootstrap(page framework),D3(plot)

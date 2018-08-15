# BARD Bangla Article Classifier
Video Demo: <a href="https://bit.ly/BARD_VIDEO_DEMO"> bit.ly/BARD_VIDEO_DEMO </a> <br/>
Dataset Link: <a href="https://bit.ly/BARD_DATASET"> bit.ly/BARD_DATASET </a> <br/>

<h2>Dataset Details</h2>
<table>
<tr>
<td align="center">Category  </td><td align="center">  No. of Documents  </td><td align="center">  No. of Words  </td><td align="center">  Average Sentences per Document  </td><td align="center">  Average words per Sentence</td>
</tr><tr>
<td align="center">State </td><td align="center">  242860  </td><td align="center">  57019465  </td><td align="center">  18.50  </td><td align="center">  13.356</td>
</tr><tr>
<td align="center">Economy </td><td align="center">  18982  </td><td align="center"> 4915141  </td><td align="center">  20.18  </td><td align="center"> 13.378</td>
</tr><tr>
<td align="center">International </td><td align="center"> 32203  </td><td align="center"> 7096111  </td><td align="center">  18.47  </td><td align="center"> 12.493</td>
</tr><tr>
<td align="center">Entertainment </td><td align="center"> 31293  </td><td align="center"> 6706563  </td><td align="center">  21.70  </td><td align="center"> 10.236</td>
</tr><tr>
<td align="center">Sports </td><td align="center"> 50888 </td><td align="center"> 12397415  </td><td align="center"> 22.80  </td><td align="center"> 11.069</td>
</tr>
</table>

<h2>Abstract</h2>
In the literature article classification is well studied, where several supervised leaning models have been proposed by utilizing large textual data corpus. Despite several comprehensive textual dataset available for different language, only a few small datasets available for Bangla articles. As a result, a couple works address the Bangla document classification and could not able to learn sophisticated supervised learning model. In this work, we curated a large dataset of Bangla article which help us to train several supervised learning model using some sophisticate features, such as word2vec. As word2vec preserves semantic features, it shows superior performance in text classification. Moreover, Neural Network with word2vec features shows promising performance compared to other state-of-the-art-work in the text classification. 
<br/>Furthermore, we deployed our proposed Bangla content classifier as a web application, which is accessible <a href="http://bard2018.pythonanywhere.com">here</a>.  and the video demo of this application is available <a href="https://bit.ly/BARD_VIDEO_DEMO">here</a>. Additionally, we open-sourced the <a href="https://bit.ly/BARD_DATASET">BARD dataset</a> and source code of this work in this repository.


<h2>Statistical Analysis</h2>
<figure>
  <img src="https://raw.githubusercontent.com/tanvirfahim15/BARD-Bangla-Article-Classifier/master/images/Stop%20words.png"  style="width:100%">
  <figcaption>Figure 01: Most frequent words in each categories.</figcaption>
</figure>
<figure>
  <img src="https://raw.githubusercontent.com/tanvirfahim15/BARD-Bangla-Article-Classifier/master/images/WO%20Stop%20words.png"  style="width:100%">
  <figcaption>Figure 02: Most frequent words in each categories after removing stop words.</figcaption>
</figure>


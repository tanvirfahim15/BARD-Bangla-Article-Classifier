# BARD Bangla Article Classifier
Video Demo: <a href="https://bit.ly/BARD_VIDEO_DEMO"> bit.ly/BARD_VIDEO_DEMO </a> <br/>
Dataset Link: <a href="https://bit.ly/BARD_DATASET"> bit.ly/BARD_DATASET </a> <br/>

<h2>Dataset Details</h2>
<table align="center">
<tr>
<td>Category  </td><td>  No. of Documents  </td><td>  No. of Words  </td><td>  Average Sentences per Document  </td><td>  Average words per Sentence</td>
</tr><tr>
<td>State </td><td>  242860  </td><td>  57019465  </td><td>  18.50  </td><td>  13.356</td>
</tr>
</table>



CategoryNo.  ofDocumentsNo.  ofWordsAverageSentencesperDocumentAveragewordsperSentenceState2428605701946518.5013.356Economy18982491514120.1813.378International32203709611118.4712.493Entertainment31293670656321.7010.236Sports508881239741522.8011.069




In the literature article classification is well studied, where several supervised leaning models have been proposed by utilizing large textual data corpus. Despite several comprehensive textual dataset available for different language, only a few small datasets available for Bangla articles. As a result, a couple works address the Bangla document classification and could not able to learn sophisticated supervised learning model. In this work, we curated a large dataset of Bangla article which help us to train several supervised learning model using some sophisticate features, such as word2vec. As word2vec preserves semantic features, it shows superior performance in text classification. Moreover, Neural Network with word2vec features shows promising performance compared to other state-of-the-art-work in the text classification. 
    \par Furthermore, we deployed our proposed Bangla content classifier as a web application, which is accessible at \url{www.bard2018.pythonanywhere.com}  and the video demo of this application is available here: \url{bit.ly/BARD_VIDEO_DEMO}. Additionally, we open-sourced the BARD dataset(\url{bit.ly/BARD_DATASET}) and source code of this work().

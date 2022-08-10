# Big-Data-Research-Project
Research on Drug recommendation system based on sentimental analysis

The primary data is Drug review data set from the UCI machine learning repository. The dataset provides patient reviews on specific drugs along with related conditions and a 10 star patient rating reflecting overall patient satisfaction. The data was obtained by crawling online pharmaceutical review sites (Drugs.com).  

# Results

The results generated by the model is generated by analysing the sentimental analysis of the drug reviews for each health condition. To evaluate the sentiments of the reviews, the positive sentiments are considered as value 1 and negative sentiments as value 0. The mean of each drug per health condition is calculated and drugs with the highest mean for a particular health condition are predicted. We are evaluating the results using sequential neural network and sequential neural network with LightGBM. We can observe that sequential neural network with LightGBM model gives the best accuracy. The sequential neural network with LightGBM model recommends drugs to the health conditions based on the analysis and evaluation of reviews with the accuracy of 84.3 percentage.

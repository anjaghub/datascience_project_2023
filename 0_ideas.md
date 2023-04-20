# Ideas


## Beginning
- Exploratory Data Analysis (Project/Data Understanding)
    - Data types, summary statistics (samples of very high scorers)
    - Sentiment over time
    - Languages used
    - Which subreddits are particularly active regarding climate crisis (pos/negative)
    - Correlations (sentiment score and voting score, maybe also with absolute value of sentiment)
    - Wordclouds (maybe also for subgroups with certain keywords)
- Data Preparation/Feature engineering
    - Select data sample (?)
        - e.g. recent posts/comments, only those where posts can be combined with comments
    - Sentiment analysis 
        - maybe on post/comments level (correlation between posts/comments if combinable?)
        - maybe train model on comments dataset with given sentiment score and apply on scraped, real-world data (including posts and comments)
    - Joining posts and comments if possible ("network analysis")
        - only comments have sentiment score!
    - Use reddit API to get more features about posts/users 
        - Problem: Anonymized usernames in post data
        - 60 requests/min (with several accounts, approx max 1 Mio. requests feasible)
        - Use PRAW (https://praw.readthedocs.io/en/latest/index.html)
    - Create features based on post/comment text
        - e.g. try to extract names, dates, events, etc.
        - extract domain from associated shared url and use as feature (could use database of trustworthy domains to compare with and create dummy)
- Modeling
    - Clustering
        - Utilizing sentiment analysis and created features
        - Clustering with processed post/user data 
        - Find clusters of activism, harassment, disinformation, etc. (try to detect suspicious users/posts -> Bot/troll detection; "Uncovering climate change bots")
            - https://arxiv.org/abs/1802.04289 - particularly interesting for tweet based detection
            - https://arxiv.org/abs/2106.13088 - pretrained detection model on github (but user based)
            - https://ieeexplore.ieee.org/document/9410535 - especially about tweet-based bot detection
        - Find characteristics of clusters
        - Evaluation difficult
    - LDA?
        - Identifying topics of documents


## Final project
- How did sentiment change over time?
    - Maybe re-do sentiment analysis with newer/more accurate methods
    - Identify major influential events on sentiment
- Which topics regarding climate change are particularly positively/negatively discussed? 
    - Word cloud per group
    - Do topic identification for positive/neutral/negative posts ("LDA")
    - Reverse search: for given topics, which are most negative/positive
- Are there any clusters in topics, sentiment, etc. (Here feature engineering comes particularly into play)
    - What characteristics do the found clusters have?

## Inofficial further tries
- Identify bots (if we have enough time/motivation)
    - Maybe find pre-trained model to detect bots
- Fetch usernames (and more) via API
    - generate graph and features based on API data
    - thus improve bot detection
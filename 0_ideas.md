# Ideas

- Exploratory Data Analysis (Project/Data Understanding)
    - data types, summary statistics (samples of very high scorers)
    - sentiment over time
    - correlations (sentiment score and voting score, maybe also with absolute value of sentiment)
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
    - create features based on post/comment text
        - e.g. try to extract names, dates, events, etc.
        - extract domain from associated shared url and use as feature (could use database of trustworthy domains to compare with and create dummy)
- Modeling: Clustering
    - utilizing sentiment analysis and created features
    - clustering with processed post/user data 
    - Find clusters of activism, harassment, disinformation, etc. (try to detect suspicious users/posts -> Bot/troll detection; "Uncovering climate change bots")
    - Find characteristics of clusters
    - Evaluation difficult
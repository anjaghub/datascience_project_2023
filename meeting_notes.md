# Meeting Notes

## 15.05.2023 Final Steps
- Yvonne mentioned the very small sample sizes for topics, problematic to show overall trends as shares would be very small (<2%)
- Discussed to still continue as planned and might change "basis"/denominator to increase share size
- Yvonne categorizing into larger groups und generating plots till Saturday before noon
- Luis adds several points to poster (u.A. framing der Ergebnisse als Vorarbeit für Sozialwissenschaften)
- Felix will add his "Senf" afterwards to finalize it till Monday the latest
- Agreed on making some final meeting before the poster pitches, probably on Wednesday

## 05.05.2023 Next Steps
- Decided on only using comments (posts have different structure, often only title no body, also relatively small sample size)
- Decided on creating separate datasets per year and limit the number of comments per year to max 100.000 (randomly chosen)
- Thus expect to have at most 1m comments in total (faster to process) 
- Decided to keep "climate" and "change" in body (and remove for specific tasks)
- Anja adapts pre-processing file accordingly
- Anja runs topic detection on final data and separately per year
    - Possible to incorporate weighting of posts by score (i.e. upvotes - downvotes) in topic selection? 
- Felix runs several text classification models (sentiment, emotion, climate is concern)
- Yvonne (/Felix) will assess final results and create some visualizations (and/or a fancy JavaScript based interactive dashboard ;)
    - Sentiment/emotion/climate-concern shares over time (in total)
    - Analysis of most prominent topics (over time)
    - Emotions/sentiment of hot topics (over time)
- Should not forget about bias, i.e. data is not representative for whole (western) population. Results based on comments probably mainly of white, young males from western countries with high screen time (-> maybe Luis can find out more about average reddit users)

## 29.04.2023 Meeting after DDS class about focus
Questions so far:
- Which topics are discussed on Reddit regarding climate change?
- How can these topics be described/characterized (e.g. in terms of their emotion, sentiment, most used words, ...)?

Extra:
- How do the topics behave over the years; are there differences? (Focus on specific years/ranges; maybe align with "history" of climate change denial)

We also discussed that:
- Empty posts, bot subreddits, duplicates and the word climate change are sorted out.
- We will use BERTopic for topic clustering.
- We will use comments, post text and post title
- Luis will do some research on Reddit and climate change discourse over time so we have some context for our results
- Anja takes care of data cleaning and topic clustering
- Felix looks into sentiment, emotion and continues to tinker with his API query which we can then use as an add on.
- Will make an individual, fancier poster

## 27.04.2023 Topic Decision
- Research questions which we want to propose:
    - Which topics are discussed on Reddit in relation to climate change?
    - How can these topics be described (e.g. in terms of their emotion, sentiment, most used words, ...)?
    Extra:
    - How do the topics behave over the years; are there changes over time?

- Empty posts, bot subreddits, duplicates and the word climate change will be sorted out
- We will use BERTopic for topic clustering
- We will use comments, post text and post title to do the analysis
- Luis will do some research on Reddit and climate change discourse over time so we can compare our results with real world knowledge
- Anja takes care of data cleaning and topic clustering
- Felix is looking into sentiment, emotion and playing with his API query which we might be able to use as an add on later
- Next week is the peer review meeting, we'll ask if we want to do it in person or not; in any case, the related questionnaire has to be filled out afterwards
- We don't want to use the "lame" poster template from DataScience department, but we want to give it a shiny update

## 18.04.2023 First Group Meeting
- Scheduled our regular meeting for Thursdays after class
- Luis found subreddits where only bots have created (a lot, a lot, a lot of) comments --> this could be used for a bot detection algorithm
- Yvonne is interested in trying clustering
- We won't meet this week anymore
- Modelling exploration till next Thursday (27.04.2023) --> decision about what we want to focus on and sending mail to Prof. Ehmke
- Discussion how we want to use GitHub and how to structure our files

## 18.04.2023 Kick Off Meeting with Project Supervisor
- We can always ask for a feedback meeting if needed
- It is fine if we want to build a sentiment score even though there is one existing for comments
- All our ideas make sense 
- We should focus on one and let Prof. Ehmke know about our decision in about a week
- Some of our data preparation ideas would also count as modelling
- We don't need to use all the data, a subset would be fine too
- Prof. Ehmke liked for example the ideas of bot detection, topic clustering, topic developement over time as well as description / sense making of clusters

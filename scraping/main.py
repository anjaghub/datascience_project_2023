import pandas as pd

import reddit_scraping as rs


def main():

    # DEFINE VARIABLES HERE
    credentials_path = "../data/credentials.json"
    data_path = "../data/"
    csv_name = "climatechaos_sample_posts.csv"

    # Load data to be extended
    df = pd.read_csv(data_path + csv_name)

    # Decide if user or post data
    scraper = rs.ScrapePosts(df, data_path, credentials_path)
    scraper.run()
    print(scraper.results[0]["author"])


if __name__ == "__main__":
    main()
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from textblob import TextBlob

def type_pie_chart(df): 
    # Assuming you have already created the DataFrame 'df' as described earlier

    # Count the occurrences of each 'type'
    type_counts = df['type'].value_counts()

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(type_counts, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of "type"')

    # Create a legend outside the circle
    plt.legend(type_counts.index, loc="center left", bbox_to_anchor=(0.75, 1))

    # Show the pie chart
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def domain_pie_chart(df):
    # Count the occurrences of each domain
    domain_counts = df['domain'].value_counts()
    
    # Calculate the total count of domains
    total_domains = len(df)
    
    # Filter domains with more than 5% of the distribution
    threshold_percentage = 5.0
    filtered_domains = domain_counts[domain_counts / total_domains * 100 > threshold_percentage]
    
    # Group other domains under "Other" and calculate their count
    other_domains_count = total_domains - filtered_domains.sum()
    if other_domains_count > 0: 
        filtered_domains['Other'] = other_domains_count

   
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(filtered_domains, startangle=140, autopct='%1.1f%%')
    plt.legend(filtered_domains.index, loc="upper left")
    plt.title('Distribution of Domains (More than 5%)')
    
    # Show the pie chart
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def domain_bar_chart(df):
    # Assuming your DataFrame is named 'df' with a 'domain' column
    domain_counts = df['domain'].value_counts().head(10)  # Display top 10 domains
    plt.bar(domain_counts.index, domain_counts.values)
    plt.xlabel('Domain')
    plt.ylabel('Count')
    plt.title('Top 10 Domains with the Most Articles')
    plt.xticks(rotation=10)  # Rotate x-axis labels for better readability
    plt.show()

def title_word_cloud(df): 
    # Create separate DataFrames for "fake" and "non-fake" news
    fake_news_df = df[df['type'] == 'fake']
    non_fake_news_df = df[df['type'] != 'fake']

    # Combine all text content into a single string for "fake" news
    fake_text = ' '.join(fake_news_df['title'].dropna())

    # Generate the word cloud for "fake" news
    wordcloud_fake = WordCloud(width=800, height=400, background_color='white').generate(fake_text)

    # Combine all text content into a single string for "non-fake" news
    non_fake_text = ' '.join(non_fake_news_df['title'].dropna())

    # Generate the word cloud for "non-fake" news
    wordcloud_non_fake = WordCloud(width=800, height=400, background_color='white').generate(non_fake_text)

    # Create subplots for both word clouds
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(wordcloud_fake, interpolation='bilinear')
    plt.axis('off')  # Remove axis
    plt.title('Word Cloud of Fake News Titles')

    plt.subplot(1, 2, 2)
    plt.imshow(wordcloud_non_fake, interpolation='bilinear')
    plt.axis('off')  # Remove axis
    plt.title('Word Cloud of Non-Fake News Titles')

    plt.tight_layout()
    plt.show()

   
def sentiment_scatter(df):
    def get_sentiment_polarity(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    # Create DataFrames for "fake" and "non-fake" news
    fake_news_df = df[df['type'] == 'fake'].copy()
    non_fake_news_df = df[df['type'] != 'fake'].copy()

    # Calculate sentiment polarity for title and content for both DataFrames
    fake_news_df['title_sentiment'] = fake_news_df['title'].apply(get_sentiment_polarity)
    fake_news_df['content_sentiment'] = fake_news_df['content'].apply(get_sentiment_polarity)
    non_fake_news_df['title_sentiment'] = non_fake_news_df['title'].apply(get_sentiment_polarity)
    non_fake_news_df['content_sentiment'] = non_fake_news_df['content'].apply(get_sentiment_polarity)

    # Calculate correlation between title and content sentiment for both DataFrames
    fake_correlation = fake_news_df[['content_sentiment', 'title_sentiment']].corr().iloc[0, 1]
    non_fake_correlation = non_fake_news_df[['content_sentiment', 'title_sentiment']].corr().iloc[0, 1]

    # Create scatter plots for "fake" and "non-fake" news with correlation in title
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(fake_news_df['content_sentiment'], fake_news_df['title_sentiment'], alpha=0.5)
    plt.xlabel('Content Sentiment')
    plt.ylabel('Title Sentiment')
    plt.title(f'Scatter Plot of Sentiment (Fake News)\nCorrelation: {fake_correlation:.2f}')

    plt.subplot(1, 2, 2)
    plt.scatter(non_fake_news_df['content_sentiment'], non_fake_news_df['title_sentiment'], alpha=0.5)
    plt.xlabel('Content Sentiment')
    plt.ylabel('Title Sentiment')
    plt.title(f'Scatter Plot of Sentiment (Non-Fake News)\nCorrelation: {non_fake_correlation:.2f}')

    plt.tight_layout()
    plt.show()

def sentiment_heatmap(df): 
    # Assuming your DataFrame 'df' has columns: 'type', 'title', and 'content'

    # Function to calculate sentiment polarity using TextBlob
    def get_sentiment_polarity(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    # Define sentiment categories
    sentiment_categories = ["Negative", "Neutral", "Positive"]

    # Define sentiment discretization function
    def discretize_sentiment(polarity):
        if polarity < -1/3:
            return "Negative"
        elif -1/3 <= polarity <= 1/3:
            return "Neutral"
        else:
            return "Positive"

    # Create DataFrames for "fake" and "non-fake" news
    fake_news_df = df[df['type'] == 'fake'].copy()
    non_fake_news_df = df[df['type'] != 'fake'].copy()

    # Calculate sentiment polarity for title and content for both DataFrames
    fake_news_df['title_sentiment'] = fake_news_df['title'].apply(get_sentiment_polarity)
    fake_news_df['content_sentiment'] = fake_news_df['content'].apply(get_sentiment_polarity)
    non_fake_news_df['title_sentiment'] = non_fake_news_df['title'].apply(get_sentiment_polarity)
    non_fake_news_df['content_sentiment'] = non_fake_news_df['content'].apply(get_sentiment_polarity)

    # Discretize sentiment into categories
    fake_news_df['title_sentiment_category'] = fake_news_df['title_sentiment'].apply(discretize_sentiment)
    fake_news_df['content_sentiment_category'] = fake_news_df['content_sentiment'].apply(discretize_sentiment)
    non_fake_news_df['title_sentiment_category'] = non_fake_news_df['title_sentiment'].apply(discretize_sentiment)
    non_fake_news_df['content_sentiment_category'] = non_fake_news_df['content_sentiment'].apply(discretize_sentiment)

    # Create pivot tables for the heatmaps and fill missing values
    pivot_fake = fake_news_df.pivot_table(index='title_sentiment_category', columns='content_sentiment_category', aggfunc='size', fill_value=0)
    pivot_fake = pivot_fake.reindex(columns=sentiment_categories, index=sentiment_categories, fill_value=0)

    pivot_non_fake = non_fake_news_df.pivot_table(index='title_sentiment_category', columns='content_sentiment_category', aggfunc='size', fill_value=0)
    pivot_non_fake = pivot_non_fake.reindex(columns=sentiment_categories, index=sentiment_categories, fill_value=0)

    # Create the subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot the heatmap for "fake" news
    sns.heatmap(pivot_fake, annot=True, fmt='d', cmap='coolwarm', cbar=True, ax=axes[0])
    axes[0].set_xlabel('Content Sentiment Category')
    axes[0].set_ylabel('Title Sentiment Category')
    axes[0].set_title('Sentiment Heatmap (Title vs. Content) - Fake News')

    # Plot the heatmap for "non-fake" news
    sns.heatmap(pivot_non_fake, annot=True, fmt='d', cmap='coolwarm', cbar=True, ax=axes[1])
    axes[1].set_xlabel('Content Sentiment Category')
    axes[1].set_ylabel('Title Sentiment Category')
    axes[1].set_title('Sentiment Heatmap (Title vs. Content) - Non-Fake News')

    plt.tight_layout()
    plt.show()


def nlp_exploratory_analysis(df): 
    """ 
        df must contain the following fields: 
            - domain 
            - type 
            - content 
            - title 
            - authors 
        
        Only these fields will be used for the exploratory analysis.
    """
    print(df)
    type_pie_chart(df)
    domain_pie_chart(df)
    domain_bar_chart(df)
    title_word_cloud(df)
    sentiment_scatter(df)
    sentiment_heatmap(df)
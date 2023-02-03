import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.preprocessing import OneHotEncoder

# remove Portuguese articles from the title
def remove_articles(title):
    articles = ['o', 'a', 'os', 'as', 'um', 'uns', 'uma', 'umas']
    title_words = title.lower().split()
    title_without_articles = [word for word in title_words if word not in articles]
    return ' '.join(title_without_articles)

#df['title'] = df['title'].apply(remove_articles)

# remove non-food related words from the title
def remove_non_food_words(title):
    non_food_words = ['com', 'de', 'e', 'em', 'grelhado', 'lactose', 'glúten', 'ralada', 'ralado', 'salada', 'frissé']
    title_words = title.lower().split()
    title_without_non_food_words = [word for word in title_words if word not in non_food_words]
    return ' '.join(title_without_non_food_words)

#df['title'] = df['title'].apply(remove_non_food_words)

def preprocess_data(df):
    # remove the articles from the title column
        #df['title'] = df['title'].apply(lambda x: x.lower().replace('[brasil]','').replace('[frança]','').replace('[espanha]','').replace('[catar]',''))
    df['title'] = df['title'].apply(remove_articles)
    
    df['title'] = df['title'].apply(remove_non_food_words)

    # convert the title column into numerical data using TfidfVectorizer
    tfidf = TfidfVectorizer()
    title_matrix = tfidf.fit_transform(df['title'].tolist())

    # Filter rows where category is 'Carne'
    #df = df[df['category'] == 'Carne']

    # Initialize the TfidfVectorizer
    #tfidf = TfidfVectorizer()

    # Fit the vectorizer on the title column and transform the data
    #tfidf_matrix = tfidf.fit_transform(df['title'])
    
    # Get the feature names
    #feature_names = tfidf.get_feature_names()

    
    # Create a new dataframe with the most important features
    #df_features = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

    # Concatenate the new dataframe with the original dataframe
    #df = pd.concat([df, df_features], axis=1)

    # Drop the original title column
    #df = df.drop(['title'], axis=1)

    # one hot encode the week_day column
    ohe = OneHotEncoder(categories='auto')
    week_day_matrix = ohe.fit_transform(df[['week_day']])
    
    # concatenate the title_matrix and week_day_matrix
    X = pd.concat([pd.DataFrame(title_matrix.toarray()), pd.DataFrame(week_day_matrix.toarray())], axis=1)
    
    # normalize the k_calories column
    k_calories_matrix = df[['k_calories']] / df[['k_calories']].max()
    
    # one hot encode the category column
    ohe = OneHotEncoder(categories='auto')
    y = ohe.fit_transform(df[['category']])
    
    return X, y

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv(r'Cardapio\\Gerado\\items2_10-12-2022 201016.csv')

# preprocess the data
X, y = preprocess_data(df)


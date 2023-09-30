import pandas as pd
import eda

# Define your data as a list of dictionaries
sample_data = [
    {
        'id': 30017,
        'domain': 'beforeitsnews.com',
        'type': 'fake',
        'content': '29\n\nBy The 2012 Scenario on Sunday Dec 31 20...',
        'title': 'Stories in the "2012" category',
        'authors': None
    },
    {
        'id': 30029,
        'domain': 'beforeitsnews.com',
        'type': 'fake',
        'content': 'Is There Something Else Going-On Many of Us ha...',
        'title': 'David Icke talks about Grenfell Fire, a “Hunge...',
        'authors': None
    },
    {
        'id': 30028,
        'domain': 'clarin.com',
        'type': 'political',
        'content': 'For fucks sake this is the worst..',
        'title': 'I am very happy',
        'authors': 'Jose Luis Espert'
    },
        {
        'id': 30028,
        'domain': 'clarin.com',
        'type': 'political',
        'content': 'Milei gana de la mano de todos los amigos...',
        'title': 'Gana gana pierde Milei',
        'authors': 'Jose Luis Espert'
    },

        {
        'id': 30028,
        'domain': 'clarin.com',
        'type': 'political',
        'content': 'Sometimes good ,sometimes bad',
        'title': 'This is the worst',
        'authors': 'Jose Luis Espert'
    }
    # Add more rows with data here
]

# Create the DataFrame
df = pd.DataFrame(sample_data)



# TODO - Hay que pasarle el df final para la entrega del TP, segun como queda formateado del notebook
eda.nlp_exploratory_analysis(df)


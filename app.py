# Importing necessary libraries
from pytube import extract  
from heapq import nlargest  
from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from spacy.lang.en.stop_words import STOP_WORDS  
from string import punctuation  

# Function to fetch and summarize YouTube video transcript
def summarize_youtube_video(url):
    
    video_id = extract.video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Combine the text from the transcript into a single string
    text = " ".join([elem["text"] for elem in transcript])

    # Load the spaCy English NLP model
    nlp = spacy.load('en_core_web_sm')
    document = nlp(text)  # Process the transcript text using the NLP model

    # Initialize a dictionary to hold word frequencies
    word_frequencies = {}
    
    # Calculate the frequency of each word in the document
    for word in document:
        text = word.text.lower()
        # Check if the word is not a stop word or punctuation
        if text not in list(STOP_WORDS) and text not in punctuation:
            word_frequencies[text] = word_frequencies.get(text, 0) + 1

    # Normalize the word frequencies
    max_frequency = max(word_frequencies.values(), default=0)
    # Divide each frequency by the maximum frequency to normalize it
    word_frequencies = {word: freq / max_frequency for word, freq in word_frequencies.items()}

    # Initialize a dictionary to hold sentence scores
    sentence_scores = {}
    
    # Score each sentence based on the word frequencies
    for sentence in document.sents:
        for word in sentence:
            if word.text.lower() in word_frequencies:
                # Increment the sentence's score based on the word's frequency
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word.text.lower()]

    # Generate summary
    select_length = int(len(list(document.sents)) * 0.3)  # Selecting 30% of total sentences for the summary
    # Select the top sentences based on their scores
    summary_sentences = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    summary = ' '.join([sentence.text for sentence in summary_sentences])
    
    return summary  

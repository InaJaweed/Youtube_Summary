# YouTube Video Transcript Summary

## Description

This is a Flask-based project that extracts transcripts from YouTube videos and generates summaries using Natural Language Processing (NLP) techniques. The project combines Flask, Python, and the Natural Language Toolkit (NLTK) to perform sentence tokenization and text summarisation.

## Project Overview

This project is designed to summarize YouTube video transcripts by identifying the most important parts of a video. Using the YouTube API, we retrieve the transcript of a specified video. Once the transcript is retrieved, we process it using NLTK to tokenize the text into sentences. Finally, we apply extractive summarization techniques to generate a concise summary, which is displayed on the web interface using Flask, a lightweight web framework for Python.

Through this project, I aim to gain a deeper understanding of how to:

- Set up a Flask project
- Define routes and handle HTTP requests
- Render HTML templates
- Interact with forms and user inputs
- Deploy a Flask application

This project is designed as a learning exercise, with a simple structure to help solidify core Flask concepts.

## Technologies Used

`Flask`: Web framework to handle HTTP requests and responses.

`YouTube API & pytube`: To retrieve video transcripts.

`NLTK`: Natural Language Toolkit for tokenization and summarization.

`youtube_transcript_api:` API for retrieving YouTube video transcripts.

## How It Works

1. Input a YouTube Video URL: The user inputs a YouTube URL in the web interface.

2. Transcript Extraction: The application fetches the transcript using the YouTube API and youtube_transcript_api.

3. Text Tokenization: The transcript is split into sentences using NLTK's sentence tokenization.

4. Summarization: The most significant sentences are selected using an extractive summarization technique.

5. Summary Display: The generated summary is displayed in the web interface.

## Future Enhancements

- Support summarization for multilingual transcripts.
- Enhance the summarization algorithm for better accuracy.
- Add user-friendly UI/UX improvements.
- Deploy the application for public access.

## Disclaimer

This project is intended for educational and practice purposes only. While efforts have been made to ensure the functionality and usability of the YouTube summariser, it is important to note that the summarisation results may not be accurate or reliable. Users should be aware that the summaries generated are based on the algorithm's interpretation of the video's transcript and may not capture the full context or nuances of the content and should not be used for critical decision-making or official purposes.

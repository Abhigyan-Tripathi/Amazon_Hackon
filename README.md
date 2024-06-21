# Amazon_Hackon
## Customer Payment Assistant
This repository provides a Python-based solution for automating customer payment interactions and recommending suitable payment options. It comprises two key components:

### Chatbot for Payment Queries (payment_chatbot.ipynb):

Manages customer inquiries related to payments.
+ Integrates with the 'payment' and 'customer_service_log' tables in the database for data retrieval.
+ Leverages a natural language processing (NLP) library (implementation details to be provided) to understand customer intent.

Provides informative responses, potentially including:
* Payment status updates
* Payment history details

### Payment Recommendation System (payment_recommendation_system.ipynb):

+ Analyzes customer payment data from the payments table in the database.
+ Employs Singular Value Decomposition (SVD) machine learning algorithm to recommend the most suitable payment method for each customer based on their payment history and 
  preferences.

Potential factors considered (customize based on your model):
 * Past payment methods used
 * Success rate
 * cashback earned

### Requirements
* Python libraries including(numpy, scikitlearn, tensorflow, flask and pandas)
* Database connection details

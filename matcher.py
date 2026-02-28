from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, job_description):
    """Calculate match score between resume and job description"""
    try:
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        
        # Combine texts for vectorization
        documents = [resume_text, job_description]
        
        # Fit and transform
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        # Convert to percentage
        score = round(similarity[0][0] * 100, 2)
        
        return score
    except Exception as e:
        print(f"Error calculating match score: {e}")
        return 0

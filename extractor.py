import re

def extract_details(text):
    """Extract key details from resume text"""
    details = {
        'name': extract_name(text),
        'email': extract_email(text),
        'phone': extract_phone(text),
        'skills': extract_skills(text),
        'education': extract_education(text),
        'experience': extract_experience(text)
    }
    return details

def extract_name(text):
    """Extract name from resume (assumes first line or prominent text)"""
    lines = text.split('\n')
    for line in lines[:5]:
        line = line.strip()
        if len(line) > 2 and len(line) < 50 and not any(char.isdigit() for char in line):
            return line
    return "Not found"

def extract_email(text):
    """Extract email using regex"""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else "Not found"

def extract_phone(text):
    """Extract phone number using regex"""
    phone_pattern = r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]'
    phones = re.findall(phone_pattern, text)
    return phones[0] if phones else "Not found"

def extract_skills(text):
    """Extract skills from resume"""
    common_skills = [
        'Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'PHP', 'Go', 'Swift', 'Kotlin',
        'HTML', 'CSS', 'React', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask', 'Spring',
        'SQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Docker', 'Kubernetes', 'AWS',
        'Azure', 'GCP', 'Git', 'Jenkins', 'CI/CD', 'Machine Learning', 'Deep Learning',
        'TensorFlow', 'PyTorch', 'Scikit-learn', 'Data Analysis', 'Excel', 'Tableau',
        'Power BI', 'Agile', 'Scrum', 'REST API', 'GraphQL', 'Microservices'
    ]
    
    found_skills = []
    text_lower = text.lower()
    
    for skill in common_skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    
    return found_skills if found_skills else ["Not detected"]

def extract_education(text):
    """Extract education information"""
    education_keywords = ['bachelor', 'master', 'phd', 'degree', 'university', 'college', 'b.tech', 'm.tech', 'mba', 'bca', 'mca']
    lines = text.split('\n')
    education = []
    
    for line in lines:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in education_keywords):
            education.append(line.strip())
    
    return education if education else ["Not found"]

def extract_experience(text):
    """Extract work experience"""
    # Look for year patterns that might indicate experience
    year_pattern = r'(19|20)\d{2}\s*[-–—]\s*(19|20)\d{2}|(19|20)\d{2}\s*[-–—]\s*present'
    experiences = re.findall(year_pattern, text, re.IGNORECASE)
    
    if experiences:
        return f"Found {len(experiences)} experience entries"
    return "Not detected"

import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bson import ObjectId
# Connexion MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_recommendation"]
cv_collection = db["cvs"]
jobs_collection = db["processed_jobs"]
recommendations_collection = db["recommendations"]
def get_cv_skills(cv_id):
    """ Récupère les compétences extraites d'un CV et les transforme en liste """
    cv = cv_collection.find_one({"_id": ObjectId(cv_id)})
    if cv and "Skills" in cv:
        skills = cv["Skills"]

        # Si les compétences sont sous forme de string, on les transforme en liste
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(",")]  # Séparer par virgule

        return skills


    return []

def get_all_jobs():
    jobs = list(jobs_collection.find({}))

    print(jobs[0])
    print(type(jobs))
    print(f"📌 [DEBUG] Nombre d'offres analysées : {len(jobs)}")  
    return jobs

def compute_similarity(cv_skills, job_skills_list):
    """ Calcule la similarité Cosine entre le CV et les offres """
    corpus = [" ".join(cv_skills)] + [" ".join(job) for job in job_skills_list]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]
    return similarities

def match_cv_to_jobs(cv_id):
    """ Associe un CV aux offres d'emploi les plus pertinentes """
    cv_skills = get_cv_skills(cv_id)
    jobs = get_all_jobs()
    job_skills_list = [job["skills"] for job in jobs]
    similarities = compute_similarity(cv_skills, job_skills_list)
    ranked_jobs = sorted(zip(jobs, similarities), key=lambda x: x[1], reverse=True)
    recommendations = [
        {
            "cv_id": str(cv_id),  
            "job_id": str(job["_id"]),  
            "job_title": job.get("jobTitle", "Titre inconnu"),
            "similarity": round(float(sim), 2),  
            "_id": str(ObjectId())  ,
            "company": job.get("company", "Entreprise inconnue"),
            "location": job.get("location", "Localisation inconnue"),
            "skills": job.get("skills", []) ,
            "contract": job.get("typeContrat", "Type de contrat inconnu"),
            "experience": job.get("experience", "Expérience inconnue"),
            "education": job.get("studyLevel", "Niveau d'études inconnu"),
            "telework": job.get("Remote", "Télétravail inconnu"),
            "publication_date": job.get("publicationDate", "Date de publication inconnue"),
            "deadline": job.get("date_limite", "Date limite inconnue"),
            "link": job.get("link", "Lien inconnu"),
            "number_of_posts": job.get("post_number", "Nombre de postes inconnu"),
        }
        for job, sim in ranked_jobs if sim > 0.2  
    ]
    if recommendations:
        recommendations_collection.insert_many(recommendations)

    return recommendations

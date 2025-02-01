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

    print(f"📌 [DEBUG] Données MongoDB pour {cv_id}: {cv}")  # 🔥 Ajout Debug

    if cv and "Skills" in cv:
        skills = cv["Skills"]

        # Si les compétences sont sous forme de string, on les transforme en liste
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(",")]  # Séparer par virgule

        return skills

    print(f"⚠️ Aucune compétence trouvée pour le CV {cv_id}")
    return []

def get_all_jobs():
    """ Récupère toutes les offres d'emploi avec leurs compétences et titres """
    jobs = list(jobs_collection.find({}, {"_id": 1, "skills": 1, "jobTitle": 1}))

    # Assurer que chaque job contient bien un `jobTitle`
    jobs = [
        {
            "_id": job["_id"],
            "skills": job["skills"],
            "jobTitle": job.get("jobTitle",)  # ✅ Correction ici
        }
        for job in jobs if "skills" in job and isinstance(job["skills"], list)
    ]

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
    print(jobs[0]["jobTitle"])
    job_skills_list = [job["skills"] for job in jobs]
    similarities = compute_similarity(cv_skills, job_skills_list)
    ranked_jobs = sorted(zip(jobs, similarities), key=lambda x: x[1], reverse=True)
    print(ranked_jobs[0][0])
    print(type(ranked_jobs[0]))
    print(ranked_jobs)
    recommendations = [
        {
            "cv_id": str(cv_id),  
            "job_id": str(job["_id"]),  
            "job_title": job.get("jobTitle", "Titre inconnu"),
            "similarity": round(float(sim), 2),  
            "_id": str(ObjectId())  
        }
        for job, sim in ranked_jobs if sim > 0.2  
    ]

    print(f"📌 [DEBUG] Nombre de recommandations trouvées : {len(recommendations)}")  

    if recommendations:
        recommendations_collection.insert_many(recommendations)

    return recommendations

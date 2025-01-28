package services

import org.mongodb.scala.Document

object DataCleaner {
  // Nettoyer les données : suppression des champs vides, ajout des valeurs par défaut et suppression des documents avec des listes de skills vides
  def cleanData(documents: Seq[Document]): Seq[Document] = {
    // Filtrer les documents avec des listes de skills non vides
    val filteredDocuments = documents.filter { doc =>
      doc.get("skills").exists(skills => {
        val skillsArray = skills.asArray().getValues
        skillsArray != null && !skillsArray.isEmpty // Vérifier que la liste des skills n'est pas vide
        import scala.collection.JavaConverters._
        skillsArray.asScala.nonEmpty
      })
    }

    // Transformer les documents restants
    filteredDocuments.map { doc =>
      val id = doc.get("_id").map(_.asObjectId().getValue.toHexString).getOrElse("unknown_id")
      val jobTitle = doc.get("job_title").map(_.asString().getValue).getOrElse("Unknown Title")
      val location = doc.get("location").map(_.asString().getValue).getOrElse("Unknown Location")
      val skills = doc.get("skills").map(_.asArray().toString).getOrElse("[]")

      Document(
        "_id" -> id,
        "job_title" -> jobTitle,
        "location" -> location,
        "skills" -> skills,
        "processed_date" -> java.time.LocalDate.now().toString
      )
    }.distinct
  }
}

package services
import scala.jdk.CollectionConverters._
import org.mongodb.scala.Document
import org.mongodb.scala.bson.BsonArray
import org.mongodb.scala.bson.BsonString
import org.mongodb.scala.bson.BsonDateTime
import java.time.format.DateTimeFormatter
import java.time.{Instant, LocalDate, ZoneId}
import org.apache.hadoop.shaded.org.checkerframework.checker.regex.qual.Regex
import scala.util.matching
object DataCleaner {
  def cleanData(documents: Seq[Document]): Seq[Document] = {
    val dateFormatter: DateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    val pattern: matching.Regex = """\d+""".r // Regex pour extraire les nombres
    // filter doculents with skills empty 
    val filteredDocuments = documents.filter { doc =>
      doc.get("competences_cles").map(_.asArray().size()).getOrElse(0) > 0
    }
    filteredDocuments.map { doc =>
      val id = doc.get("_id").map(_.asObjectId().getValue.toHexString).getOrElse("unknown_id")
      val jobTitle = doc.get("titre").map(_.asString().getValue).getOrElse("Unknown Title")
      val company = doc.get("entreprise").map(_.asString().getValue).getOrElse("Unknown Company")
      val location = doc.get("localisation").map(_.asString().getValue).getOrElse("Unknown Location") 
      val skills = doc.get("competences_cles").map {
  case array: BsonArray => array.getValues.asScala.map(_.asString().getValue).mkString(", ")
  case _ => "[]"
}.getOrElse("[]").split(",").toList
      val typeContrat = doc.get("contrat_propose").map(_.asString().getValue).getOrElse("Unknown Contract Type")
      val studyLevel = doc.get("niveau_etudes_requis").map(_.asString().getValue).getOrElse("Unknown Study Level")
      val experience = doc.get("niveau_experience").map(_.asString().getValue).getOrElse("Unknown Experience")
      // type date 
val publicationDate: String = doc.get("date_publication").collect {
  case date: BsonDateTime =>
    Instant.ofEpochMilli(date.getValue) // Convertir en Instant
      .atZone(ZoneId.of("UTC")) // Appliquer le fuseau horaire
      .toLocalDate // Extraire uniquement la date (sans heure)
      .format(dateFormatter) // Formater en "yyyy-MM-dd"
}.getOrElse("Unknown Publication Date")

// Transformer `date_limite`
val dateLimite: String = doc.get("date_limite").collect {
  case date: BsonDateTime =>
    Instant.ofEpochMilli(date.getValue)
      .atZone(ZoneId.of("UTC"))
      .toLocalDate
      .format(dateFormatter)
}.getOrElse("Unknown Deadline Date")
      val post_number = pattern.findFirstIn(doc.get("nombre_postes").map(_.asString().getValue).getOrElse("1")).getOrElse("1").toInt
      // non : false, oui : true
      val Remote = doc.get("teletravail").map(_.asString().getValue).map {
        case "Oui" => true
        case "Non" => false
        case _ => false
      }.getOrElse(false)

      val link = doc.get("lien").map(_.asString().getValue).getOrElse("Unknown Link")
      Document(
        "_id" -> id,
        "jobTitle" -> jobTitle,
        "company" -> company,
        "location" -> location,
        "skills" -> skills,
        "typeContrat" -> typeContrat,
        "studyLevel" -> studyLevel,
        "experience" -> experience,
        "publicationDate" -> publicationDate,
        "date_limite" -> dateLimite,
        "post_number" -> post_number,
        "Remote" -> Remote,
        "link" -> link,
        "processed_date" -> java.time.LocalDate.now().toString
      )
    }.distinct
  }
}
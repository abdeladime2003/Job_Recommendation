package services

import org.mongodb.scala._
import org.mongodb.scala.model.Filters._
import org.mongodb.scala.model.Updates._
import config.MongoConfig

import scala.concurrent.Await
import scala.concurrent.duration._

object MongoService {
  val mongoClient: MongoClient = MongoClient(MongoConfig.mongoUri)
  val database: MongoDatabase = mongoClient.getDatabase(MongoConfig.databaseName)
  val sourceCollection: MongoCollection[Document] = database.getCollection(MongoConfig.sourceCollection)
  val processedCollection: MongoCollection[Document] = database.getCollection(MongoConfig.processedCollection)

  // 🔹 Récupérer uniquement les jobs où processed = false
  def fetchNewJobs(): Seq[Document] = {
    val filter = equal("processed", false) // On ignore ceux où processed n'existe pas
    val future = sourceCollection.find(filter).toFuture()
    Await.result(future, 10.seconds)
  }

// 🔹 Vérifier si une offre existe déjà dans la collection processed_jobs
  def jobExists(link : String): Boolean = {
    val filter = and(equal("link", link))
    val future = processedCollection.find(filter).first().toFuture()
    val result = Await.result(future, 5.seconds)
    result != null // Si un document est trouvé, retourne true, sinon false
  }

  // 🔹 Insérer les offres nettoyées seulement si elles n'existent pas encore
  def insertProcessedData(processedData: Seq[Document]): Unit = {
    val newData = processedData.filter { doc =>
      val link = doc.get("link").map(_.asString().getValue).getOrElse("")
      !jobExists(link) // On insère uniquement si l'offre n'existe pas déjà
    }

    if (newData.nonEmpty) {
      val future = processedCollection.insertMany(newData).toFuture()
      Await.result(future, 10.seconds)
      println(s"Inserted ${newData.size} new job offers into processed_jobs.")
    } else {
      println("No new job offers to insert. All already exist.")
    }
  }

  // 🔹 Marquer les données comme traitées après traitement
  def markAsProcessed(ids: Seq[String]): Unit = {
    val future = sourceCollection.updateMany(
      in("_id", ids.map(id => new org.bson.types.ObjectId(id)): _*),
      set("processed", true)
    ).toFuture()
    Await.result(future, 10.seconds)
  }
}

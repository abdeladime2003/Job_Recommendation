package services

import org.mongodb.scala._
import config.MongoConfig

import scala.concurrent.Await
import scala.concurrent.duration._

object MongoService {
  val mongoClient: MongoClient = MongoClient(MongoConfig.mongoUri)
  val database: MongoDatabase = mongoClient.getDatabase(MongoConfig.databaseName)
  val sourceCollection: MongoCollection[Document] = database.getCollection(MongoConfig.sourceCollection)
  val processedCollection: MongoCollection[Document] = database.getCollection(MongoConfig.processedCollection)
  def fetchSourceData(): Seq[Document] = {
    val future = sourceCollection.find().toFuture()
    Await.result(future, 10.seconds)
  }

  // Insérer des données dans la collection processed
  def insertProcessedData(processedData: Seq[Document]): Unit = {
    val future = processedCollection.insertMany(processedData).toFuture()
    Await.result(future, 10.seconds)
  }
}

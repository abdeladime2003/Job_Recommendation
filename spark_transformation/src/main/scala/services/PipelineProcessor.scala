package services

import org.mongodb.scala.Document

object PipelineProcessor {
  def executePipeline(): Unit = {
    // Étape 1 : Récupérer les données de la collection source
    val rawData: Seq[Document] = MongoService.fetchSourceData()

    // Étape 2 : Nettoyer les données
    val cleanedData: Seq[Document] = DataCleaner.cleanData(rawData)

    // Étape 3 : Insérer les données nettoyées dans la collection processed
    MongoService.insertProcessedData(cleanedData)

    println(s"Pipeline executed successfully! Processed ${cleanedData.size} documents.")
  }
}

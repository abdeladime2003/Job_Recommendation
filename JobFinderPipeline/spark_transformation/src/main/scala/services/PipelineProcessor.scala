package services

import org.mongodb.scala.Document

object PipelineProcessor {
  def executePipeline(): Unit = {
    // Étape 1 : Récupérer les nouvelles offres non traitées
    val rawData: Seq[Document] = MongoService.fetchNewJobs()

    if (rawData.nonEmpty) {
      println(s"Processing ${rawData.size} new job offers...")

      // Étape 2 : Nettoyage des données
      val cleanedData: Seq[Document] = DataCleaner.cleanData(rawData)

      // Étape 3 : Insertion des données traitées dans processed_jobs
      MongoService.insertProcessedData(cleanedData)

      // Étape 4 : Mettre à jour processed = true
      val processedIds = rawData.map(_.get("_id").get.asObjectId().getValue.toHexString)
      MongoService.markAsProcessed(processedIds)

      println("Pipeline execution completed successfully!")
    } else {
      println("No new job offers to process.")
    }
  }
}

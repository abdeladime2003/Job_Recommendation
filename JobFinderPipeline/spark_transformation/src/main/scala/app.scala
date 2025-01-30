package main.scala

// Import nécessaire pour exécuter le pipeline
import services.PipelineProcessor

object App {
  def main(args: Array[String]): Unit = {
    try {
      PipelineProcessor.executePipeline()
      System.exit(0)
    } catch {
      case e: Exception =>
        println(s"Erreur lors de l'exécution du pipeline : ${e.getMessage}")
        e.printStackTrace()
        System.exit(1)
    }
  }
}

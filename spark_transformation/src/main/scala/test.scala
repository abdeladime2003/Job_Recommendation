import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object SparkMongoTest {
  def main(args: Array[String]): Unit = {
    // Création de la SparkSession
    val spark = SparkSession.builder()
      .appName("MongoDB-Spark-Test")
      .master("local[*]")
      .config("spark.mongodb.read.connection.uri", "mongodb://localhost:27017/job_recommendation.cvs")
      .config("spark.executorEnv.LC_ALL", "en_US.UTF-8")
      .config("spark.executorEnv.LANG", "en_US.UTF-8")
      .config("spark.driver.extraJavaOptions", "-Dlog4j2.configuration=file:spark_transformation/src/main/resources/log4j2.properties") // Ajout ici
      .getOrCreate()
    // Chargement des données depuis MongoDB
    val cvsDF = spark.read
      .format("mongodb")
      .load()

    // Nettoyage de la colonne Skillss
    val cleanedDF = cvsDF
      .withColumn("Skills", regexp_replace(col("Skills"), "´┐¢", "é"))

    // Afficher uniquement la colonne Skills nettoyée
    cleanedDF.select("Skills").show(truncate = false)

    // Arrêter Spark
    spark.stop()
  }
}

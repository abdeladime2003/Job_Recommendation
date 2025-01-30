package models

case class JobOffer(
  _id: String,
  jobTitle: String,
  location: String,
  skills: Seq[String],
  processedDate: Option[String] = None
)

package main.scala

import services.PipelineProcessor

object App {
  def main(args: Array[String]): Unit = {
    PipelineProcessor.executePipeline()
  }
}

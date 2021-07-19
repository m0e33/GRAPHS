from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
  logging.info("\n*************************************************\n"
               "*                                               *\n"
               "*             starting experiment               *\n"
               "*                                               *\n"
               "*************************************************\n")

  configuration_files = [
    'configuration-email-core-graphtools.yml',
    'configuration-email-core-networkx.yml',
    'configuration-email-core-snap.yml',
    'configuration-dbpl-networkx.yml',
    'configuration-dbpl-graphtools.yml',
    'configuration-dbpl-snap.yml',
    'configuration-wiki-topcats-networkx.yml',
    'configuration-wiki-topcats-graphtools.yml',
    'configuration-friendster-networkx.yml',
    'configuration-friendster-graphtools.yml',
  ]

  for configuration in configuration_files:
    logging.info("Starting to run '" + configuration + "'\n")
    benchmarks = create_benchmarks_from_config(configuration)
    runner = BenchmarkRunner(benchmarks)
    try:
      runner.run()
    except Exception as e:
      logging.error("Failed to RUN '" + configuration + "': " + str(e))

    try:
      runner.evaluate()
    except Exception as e:
      logging.error("Failed to EVALUATE '" + configuration + "': " + str(e))

    try:
      runner.collect_results()
    except Exception as e:
      logging.error("Failed to COLLECT_RESULTS for '" + configuration + "': " + str(e))
    logging.info("Finished to run '" + configuration + "'\n")


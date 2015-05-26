"""
Here are some things to keep in mind regarding logging in Twisted:
• log.startLogging 
  Use to start logging to a file, either directly or through a convenience class like DailyLogFile .
• log.msg and log.err . 
  Events are logged with log.msg & logerr, By default, log.startLogging will also redirect stdout and stderr to the log.
• log.addObserver 
  Use to register custom loggers.
• When you are writing custom log observers, never block, or your whole event loop
  will block. The observer must also be thread-safe if it is going to be used in multithreaded programs.
• Applications run with twistd have logging enabled automatically. 
  Logging can be customized through --logfile, --syslog, and --logger.
"""
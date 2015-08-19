# python-log-trimmer
Tools to trim log files out of a logged directory.  This is to prevent obvious issues such as flooding a machine with logs.

### General Usage
You'll set ```logtrimmer.py``` to run on a daily basis (weekly would work fine as well).  You'd change the config.yaml files so that it knows the directry to target, the names of the log files, and how many log files you want to keep.

### Configuration
Take a look at ```config.yaml``` it should explain it pretty well

### Testing
Set everything up, then import the file and run ```trim_log_files(test=True)```, that way it will only tell you what it's going to do.

### Automated Configuration
#### OS X
Add the ```com.log.trimmer.plist``` file to your plist, or use some other automated method to start up the file.  It will look for the config file in the same folder that the python script is in.

#### Windows
Have not used it here yet, please give me a PL with some instructions.

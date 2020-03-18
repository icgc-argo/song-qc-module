# song-qc-module
A QC module for Song that performs icgc-argo specific validations of song submissions

**Creating a verifier program**

There is a sample verifier program (written in Python) named *verifier.py* -- just edit it to create whatever verifier program you like.

_verifier.py_ must define a single function, called **verify()**. The **verify()** function must take a string containing JSON as input, and must return a list of issues (strings describing problems with the input). If there are no issues, **verify()** must return an empty list.

**Testing:**

Files which contain sample inputs for which the verifier program should fail (produce issues) should be placed into the directory tests/failing. Files which contain sample inputs for which it should produce no issues should be placed into the directory tests/passing.

To run the tests, run 

```
python3 -m pytest -s -v
```

**To run the REST Server**

When the Dockerfile is run, it creates a REST server on port 8080 which calls verifier.py to verify JSON data which is POSTED to it, and which returns the issues detected in JSON format.

*To run the dockerfile, run*

```
docker build . -t sidecar
docker run -p 8080:8080 sidecar
```

**To use with SONG**

Add the URL of your REST Server to the SONG setting *verifierURLs* in **application.properties** or **application.yaml** configuration file.


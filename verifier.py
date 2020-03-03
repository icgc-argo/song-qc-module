#!/usr/bin/env python3
import json


# fictional example verifier
def verify(message):
    errs = []
    j = json.loads(message)
    if 'files' not in j:
        errs.append('Analysis has no files section!')
        files = []
    else:
        files = j['files']
        if j['analysisType']['name'] == 'variantCall' and len(files) < 2:
            errs.append('You must include at least two files for a variant call')

    for f in files:
        if f['fileType'] == 'BAM':
            index_file = f['fileName'].replace('bam', 'bai')
            if index_file not in [i['fileName'] for i in files]:
                errs.append('You must include an index file for file "{}"'.format(f['fileName']))
        elif f['fileType'] == 'XML':
            raise Exception("Demonstrate exception handling")

        if 'fileMd5sum' not in f:
            errs.append('You must include the md5sum for file "{}"'.format(f['fileName']))
    return errs

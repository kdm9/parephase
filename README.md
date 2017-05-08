PAREphase
=========

Detects phasing around stop sites in 5'PARE data


Free for all users under the MPL v2, see ./LICENSE.


## Install

```bash
pip install parephase
```


## Usage


```shell
$ parephase --help
parephase -- Histogram coverage of 5' PARE data around stop sites

USAGE:
    parephase [options] -g GFF_FILE BAMFILE

OPTIONS:
    -P          Output counts per gene
    -u INT      Count INT bases upstream of the stop [default: 100]
    -d INT      Count INT bases downstream stream of the stop [default: 100]
    -g GFFFILE  GFF file describing gene models.
    -l GENIDS   File containing a list of gene models. If not given, all gene
                models are used, which can create inaccuate results. Please
                provide a list of representative gene models.
```

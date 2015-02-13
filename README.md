STIGMA 
-------
![status]

Easy Python program to parse OpenSCAP result files and give results. Like the following:

![alt text][sampleout]

## Instructions

- Install OpenSCAP
    
    yum install openscap-utils

- Download SCAP DISA STIG zip file from [here][0]

- Unzip DISA STIG content

- Evaluate your favorite profile, for example MAC-1_Public, and write XCCDF results into a results.xml file.

```shell
    # Example
    oscap xccdf eval --profile MAC-1_Public --results results.xml --cpe U_RedHat_5_V1R2_STIG_Benchmark-cpe-dictionary.xml U_RedHat_5_V1R2_STIG_Benchmark-xccdf.xml
```

- Run STIGMA

```shell
    python stigma.py -P /path/to/results.xml 
```

6. Optional Flags:
  *  -T Integer representing acceptable pass percentage of all benchmarks Combined
  *  -H Integer representing acceptable pass percentage of High Severity Benchmarks
  *  -M Integer representing acceptable pass percentage of Medium Severity Benchmarks
  *  -L Integer representing acceptable pass percentage of Low Severity Benchmarks









[0]:http://iase.disa.mil/stigs/scap/Pages/index.aspx
[sampleout]:https://raw.githubusercontent.com/nousdefions/STIGMA/master/sample_out.png "Sample Results" 
[status]:https://codeship.com/projects/68c0e940-95e5-0132-ce8c-1ea94e73e3c0/status?branch=master

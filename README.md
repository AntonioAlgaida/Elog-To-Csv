# Elog-To-Csv

This file changes the **omnet++ .elog** file to the **.csv** file.  
Because the .elog file that omnet++ provides when it is simulated is very **heavy**, I have decided to create a python script, which selects lines that are necessary for my application and saves part of these lines in some variables`tx_index` and `rx_index`.
Finally, these variables (`rx_frames` and `tx_frames`) are saved in .csv format for later appropriate treatment.

## Usage

An example of use is provided with the file `WE1-64-Tprobe-64-20.elog`, which can be seen that it has a size of 60MB and the final variables have a size of 47 KB and 5 KB (`WE1-64-Tprobe-64-20-rx_frames` and `WE1-64-Tprobe-64-20-tx_frames`)

## History

* 1.0 (23/05/2018)
    * Create the .elog to .csv converter
* 0.0.1 (23/05/2018)
    * Create repository

## Author

Antonio Guillen-Perez
PDH student - Technical University of Cartagena. Spain
contact: antonio.guillen@edu.upct.es

## License

See the `LICENSE.md` file for details

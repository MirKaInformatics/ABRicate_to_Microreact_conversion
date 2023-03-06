# ABRicate_to_Microreact_conversion

This is a script for converting ABRicate output into a presence/absence matrix for visualising in Microreact.

The script works with any of the ABRicate database, given that the data is in csv format (default). 
The script will set the gene as present with a match over an 80% threshold, ignoring redundancy.  
During the conversion, the script will also ask you to insert your preferred HEX codes for the colours you want in your final presence/absence matrix. 
The script will ignore your two first columns, allowing Microreact to set up colours based on strain ID corresponding with the same strain ID in your tree file. 
If you want Microreact to colour your tree based on MLST, I suggest adding in the MLST column after converting the data. 


For ABRicate, please see https://github.com/tseemann/abricate.
The data visualisation can be done in Microreat at https://microreact.org/. 

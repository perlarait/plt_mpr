Attributions:
  License - GNU v3
  Funding - Perlara, PBC
  Python scripting - Zach Parton
  Director - Sangeetha Iyer

NB: This software was designed by Perlara, PBC in order to map the contents of Supplier supplied source files (including structural information, chemical source, form, etc) to "source" plates to-be mapped for mass-scale small-molecule screening. CURRENTLY ONLY WORKS MAPPING 96->384 well plates

General Workflow:
    1) Load chemical Supplier source file into SDF reader tool, such as the open-source DATAWARRIOR 
    (http://www.openmolecules.org/datawarrior/download.html)
    
    2) Delete all columns but ID, supplier plate, and position (i.e. well).
    
    3) Export the sdf file as a txt (or directly to csv if availible).
        3.5) if export to csv is not availible, the program can run with a txt. However, it is recommended to open the txt file with a calc program, such as the open-source LIBREOFFICE CALC (https://www.libreoffice.org/download/download/) and re-save as a csv (Its strongly not recommended to simply change the file extension as it could corrupt the file esp. on M$)
    
    6) MAKE SURE THE WELL-COLUMN IN THE SOURCE PLATES FILE (src file) IS LABELED POSITION - this will be fixed in later versions.
    
    5) Run the program! Point towards your csv file (you can copy the file from a file-browser and it should insert the path on windows, mac, and most linux distros).
    
    6) your final file is in the root plt_mpr folder, called "final.csv"

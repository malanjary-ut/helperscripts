# helperscripts

These scripts are used for the collection and annotation of results generated from the gene cluster similarity applicaiton BiG-SCAPE (https://git.wageningenur.nl/medema-group/BiG-SCAPE)

allbigscapenodes:

	collects all networked clusters for each BGC class (NRPS, PKS, Terpene, ...) and combines them into a single network tab seperated document.

	python allbigscapenodes.py --help (view all options)

	example running from the "networks_all" folder. Collects all clusters with distance between 0-0.5:
	python allbigscapenodes.py -c "0-0.5"

convert2gml:

	Converts tab seperated networked nodes into gml format. Adds node annotations and extra meta data using a tab seperated file.

	python convert2gml.py --help (view all options)

	example with adding basic BGC class anotations generated in BiG-SCAPE:

	python convert2gml.py -sh -aa summary.annotations.tsv summary.network.0-0.5.tsv

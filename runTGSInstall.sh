#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

echo "Welcome to the TGSolution Pack Installer....."
echo '  This package will install TigerGraph modules (graph and data) onto any install'
echo '  of TigerGraph - local/EC2/TGCloud'
echo ''
echo "Would you like to install a Customer Demo or a TigerGraph Starter Kit?"
echo ''
read -p "  Enter Custom Demo/Starter Kit - C/c/S/s: " choice
if [[ "$choice" == *"S"* || "$choice" == *"s"* ]]; then
	cd starterKits
	./tgSolutionKitInstall.sh
	exit 0
fi

echo "For a Custom Demo install, lets make sure TG is running on this host..."

command -v gadmin >/dev/null 2>&1 || { echo >&2 "TigerGraph is not installed on this host, aborting."; exit 1; }

## ensure tg is running and gsql is available
resp=$(gsql -v)
if [[ "$resp" == *"refused"* || "$resp" == *"not found"* ]]; then
    echo "Tigergraph does not appear to be running on this host, please start it using gadmin."
    exit 2
fi

echo ''
echo "Custom demo install process "
echo ""
echo "1     - Entity Resolution(MDM)"
echo "2     - Fraud Detection"
echo "3     - LDBC Benchmark"
echo "4     - TPC-DS Benchmark"
echo "5     - Synthea HealthCare"
echo '6     - IMDB'
echo "7     - Customer360"
echo '8     - Recommendations'
echo '9     - AML Sim'
echo '10    - Ontime Flight Performance'
echo '11    - Adworks'
echo '12    - NetoworkIT Impact Analysis Graph'
echo "A/a   - Install all of the packs"
echo "Q/q   - To exit the script"
echo "mysql - Stage all of the source data to a local mysql db - NOTE assumes you have mysql installed and accessible..."
echo ''

while true; do
read -p "Pick a number, or enter a/A for all: " choice

	case $choice in

		1)
			echo ''
			echo "Install Entity Resolution (MDM)"
			gsql packages/entityResMDM/scripts/01-create-schema.gsql
			gsql packages/entityResMDM/scripts/02-load-data.gsql
			gsql packages/entityResMDM/scripts/03-add-queries.gsql
			break
		    ;;
		2)
		    echo "Install Anti-Fraud (AML)"
			gsql packages/fraud/scripts/01-create-schema.gsql
			gsql packages/fraud/scripts/02-load-data.gsql
			break
		    ;;
		3)
			echo ''
			echo "Install LDBC - with small sample dataset"
			gsql packages/ldbc/scripts/01-create-schema.gsql
			gsql packages/ldbc/scripts/02-load-data-sample.gsql
			break
		    ;;
		4)
		    echo ''
		    echo "Install TPC-DS"
			gsql packages/tpcds/scripts/01-create-schema.gsql
			gsql packages/tpcds/scripts/02-load-data.gsql
			break
		    ;;
		5)
		    echo ''
		    echo "Install Synthea"
			gsql packages/synthea/scripts/createSyntheaSchema.gsql
			./packages/synthea/scripts/installLoadJobs.sh
			gsql packages/synthea/scripts/runSyntheaLoadJobs.gsql
			break
		    ;;
		6)
		    echo ''
		    echo "Install IMDB"
		    gsql packages/imdb/scripts/01-create-schema.gsql
		    gsql packages/imdb/scripts/02-load-data.gsql
			break
		    ;;
		7)
		    echo ''
		    echo "Install Cust360"
		    ./packages/cust360/installCust360.sh
			break
		    ;;
		8)
		    echo ''
		    echo "Install Recommendations"
			gsql packages/recommendations/scripts/01-create-schema.gsql
			gsql packages/recommendations/scripts/02-load-data.gsql
			break
		    ;;
		9)
		    echo ''
		    echo "Install AML Sim"
			gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
			gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
			break
		    ;;
		10)
		    echo ''
		    echo "Install Ontime Perf Graph"
			gsql work-in-progress/airline/scripts/01-create-schema.gsql
			gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
			break
		    ;;
		11)
		    echo ''
		    echo "Install Adworks Graph"
			gsql work-in-progress/adWorks/scripts/01-create-schema.gsql
			break
		    ;;
		12) 
		    echo ''
		    echo "Install NetoworkIT Impact Analysis Graph"
			gsql packages/NetworkITResOpt/scripts/01-create-schema.gsql
			gsql packages/NetworkITResOpt/scripts/02-load-data.gsql
			break
			;;
		13) 
		    echo ''
		    echo "Install Shortest Path Flights Graph"
			gsql packages/shortestPathFlights/scripts/01-create-schema.gsql
			gsql packages/shortestPathFlights/scripts/02-load-data.gsql
			break
			;;
		a|A)
		    echo ''
		    echo 'Lets load all of the schemas'
			gsql packages/entityResMDM/scripts/01-create-schema.gsql
			gsql packages/entityResMDM/scripts/02-load-data.gsql
			gsql packages/entityResMDM/scripts/03-add-queries.gsql
		    echo "Install Fraud/AML - data tbd"
			gsql packages/fraud/scripts/01-create-schema.gsql
			gsql packages/fraud/scripts/02-load-data.gsql
			echo ''
			echo "Install LDBC - with small sample dataset"
			gsql packages/ldbc/scripts/01-create-schema.gsql
			gsql packages/ldbc/scripts/02-load-data-sample.gsql
		    echo ''
		    echo "Install TPC-DS - data tbd"
			gsql packages/tpcds/scripts/01-create-schema.gsql
			gsql packages/tpcds/scripts/02-load-data.gsql
		    echo ''
		    echo "Install Synthea"
			gsql packages/synthea/scripts/createSyntheaSchema.gsql
			./packages/synthea/scripts/installLoadJobs.sh
			gsql packages/synthea/scripts/runSyntheaLoadJobs.gsql
		    echo ''
		    echo "Install IMDB"
		    gsql packages/imdb/scripts/01-create-schema.gsql
		    gsql packages/imdb/scripts/02-load-data.gsql
		    echo ''
		    echo "Install Cust360"
		    ./packages/cust360/installCust360.sh
		    echo ''
		    echo "Install Recommendations"
			gsql packages/recommendations/scripts/01-create-schema.gsql
			gsql packages/recommendations/scripts/02-load-data.gsql
		    echo ''
		    echo "Install AML Sim"
			gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
			gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
		    echo "Install Ontime Perf Graph"
			gsql work-in-progress/airline/scripts/01-create-schema.gsql
			gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
		    echo ''
		    echo "Install Adworks Graph"
			gsql work-in-progress/adWorks/scripts/01-create-schema.gsql
		    echo ''
		    echo ''
		    echo "Install NetoworkIT Impact Analysis Graph"
			gsql packages/NetworkITResOpt/scripts/01-create-schema.gsql
			gsql packages/NetworkITResOpt/scripts/01-create-schema.gsql
		    echo ''
		    echo "Install Shortest Path Flights Graph"
			gsql packages/shortestPathFlights/scripts/01-create-schema.gsql
			gsql packages/shortestPathFlights/scripts/02-load-data.gsql
			break
		    ;;
		mysql)
		    echo ''
		    echo 'Lets stage all of the schemas to mysql'
		    echo ''
		    ./mcySQLSetup.sh
		    echo ''
			break
		    ;;
		q)
			echo 'exiting installer...'
			break
			;;
		Q)
			echo 'exiting installer...'
			break
			;;		
		*) 
			echo "Sorry, $choice is an invalid option, enter a valid option."
	    	;;
	esac
done

echo ''
echo 'Finished with setup....'
echo ''

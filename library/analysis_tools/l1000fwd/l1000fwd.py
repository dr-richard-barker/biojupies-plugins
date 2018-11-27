#################################################################
#################################################################
############### DE 
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import requests
import json
from IPython.display import display, IFrame, Markdown

##### 2. Other libraries #####


#######################################################
#######################################################
########## S1. Function
#######################################################
#######################################################

#############################################
########## 1. Run
#############################################

def run(signature, nr_genes=500, signature_label=''):

	# Define results
	l1000fwd_results = {'signature_label': signature_label}

	# Define upperGenes Function
	upperGenes = lambda genes: [gene.upper() for gene in genes]

	# Get Data
	payload = {"up_genes":upperGenes(signature.index[:nr_genes]),"down_genes":upperGenes(signature.index[-nr_genes:])}

	# Get URL
	L1000FWD_URL = 'https://amp.pharm.mssm.edu/L1000FWD/'

	# Get result
	response = requests.post(L1000FWD_URL + 'sig_search', json=payload)
	if 'KeyError' in response.text:
		l1000fwd_results['result_url'] = None
	else:
		l1000fwd_results['result_url'] = 'https://amp.pharm.mssm.edu/l1000fwd/vanilla/result/'+response.json()['result_id']

	# Return
	return l1000fwd_results

#############################################
########## 2. Plot
#############################################

def plot(l1000fwd_results, plot_counter, nr_drugs=7, height=300):
	
	# Check if results
	if l1000fwd_results['result_url']:

		# Display IFrame
		display(IFrame(l1000fwd_results['result_url'], width="1000", height="1000"))

	# Display error
	else:
		display(Markdown('### No results were found.\n This is likely due to the fact that the gene identifiers were not recognized by L1000FWD. Please note that L1000FWD currently only supports HGNC gene symbols (https://www.genenames.org/). If your dataset uses other gene identifier systems, such as Ensembl IDs or Entrez IDs, consider converting them to HGNC. Automated gene identifier conversion is currently under development.'))



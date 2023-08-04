# From https://py-readability-metrics.readthedocs.io/en/latest/


from readability import Readability

text = """"
What is personalised cancer medicine about?
Personalized medicine aims to find the best cancer treatment for the particular characteristics of each patient’s tumor. Nowadays, doctors can obtain a tumor sample using modern technology to sequence its DNA. This helps  to identify the specific mutations of the tumor and informs about treatment decisions. However, this is not an easy step since a tumor might contain hundreds of mutations. Nonetheless, it is key for the oncologist to know which mutations (usually few) are more likely to play a role in the tumor growth. This way, the best anti-cancer therapies that can target these genomic alterations can be identified. Mutations found during the tumor secuencing are complex.  Defining the mutations involved in tumor growth is a very challenging and time-consuming process. 
What if there was a tool to help interpret these cancer mutations?
We have created the tool Cancer Genome Interpreter or CGI, to  help clinicians to make the best treatment decision for their patients. The CGI is part of a project funded by the European Union where clinicians, oncology researchers and patient associations from 6 countries, including 17 institutions, joined forces to develop and improve the CGI portal. 
What is the CGI tool and CGI-Clinics?
CGI is a tool that: 1) analyzes in a safe manner mutations occurring in tumors (sudied from biopsies), and 2) identifies those cancer mutations that cause cancer progression. CGI tool is a training model. It learns directly from data from previous patients, and uses what is called machine learning algorithms. CGI was developed as a research tool by scientists at the Barcelona Biomedical Genomics lab at IRB Barcelona. CGI tool is aimed to be evolved into the clinical dessision process for cancer patients.
How can patients contribute to CGI?
In the process of improving the CGI tool, information from thousands of tumors already sequenced is needed. This way bioinformatics analysis with databases of clinical knowledge will enhance the performance of the CGI tool. CGI could then merge all this information and provide an interpretation of the mutations that will help clinicians to choose the best treatment for each patient. 
In consequence, our goal is to enrich the CGI platform with genomic data of cancer patients, and the first step would be to encourage patients to share their sequencing data. Would you help us? 
Why are we asking you to participate in this focus group?
Although sequencing data is complex. it serves as a useful tool for cancer management and disease progressionThe aim of the CGI-Clinics is  to help patients cope with the new concepts arising in personalised cancer medicine, including: next generation sequencing, tumor profiling, machine-learing, variants of unknown significance, etc. We have a team of professionals that thanks to you will identify a set of questions that are important to empower patients with, and help them be active actors both in conversations with the oncologists and in data-sharing processes with scientists.

"""
r = Readability(text)

print("Flesch Reading Ease scores are: ", r.flesch())
print("Flesch - Kincaid scores are: ", r.flesch_kincaid())
print("Gunninc Fog scores are: ", r.gunning_fog())
print("Coleman Liau scores are: ", r.coleman_liau())
print("Dale Chall scores are: ", r.dale_chall())
print("Automated Readability Index scores are: ", r.ari())
print("Linsear Write scores are: ", r.linsear_write())
#print("SMOG scores are: ", r.smog(all_sentences=True))
print("Spache scores are: ", r.spache())


# r.flesch()
# r.gunning_fog()
# r.coleman_liau()
# r.dale_chall()
# r.ari()
# r.linsear_write()
# # r.smog()
# r.spache()
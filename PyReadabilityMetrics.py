# Created by Christine Kakalou on 2/8/2023
# Project: ReadabilityScores
# Plugin from https://py-readability-metrics.readthedocs.io/en/latest/


from readability import Readability

original_text = """"

What is personalised cancer medicine about?
Personalized medicine against cancer aims to find the best cancer treatment for the particular characteristics of each patient’s tumor. Nowadays, doctors can obtain a tumor sample using modern technology to sequence its DNA, with the aim to identify the specific mutations of the tumor to inform treatment decisions. However, this is not an easy step since a tumor might contain hundreds of mutations.  It is key for the oncologist to know which mutations (usually few) are more likely to play a role in the tumor growth, to use the best anti-cancer therapies that can target these genomic alterations. Therefore, and due to the complexity of the mutations found during the tumor sequencing, defining the mutations involved in tumor growth is still a very challenging and time-consuming process. 
What if there was a tool to help interpret these cancer mutations?
We have created the tool Cancer Genome Interpreter or CGI, to help clinicians to make the best treatment decision for the patient. The CGI is part of a project funded by the European Union in which clinicians, oncology researchers and patient association from 6 countries join forces to develop and improve the CGI portal. 
What is the CGI tool and CGI-Clinics?
CGI is a tool that analyses mutations occurring in tumors (studied from biopsies) in a safe manner and identifies those cancer mutations that make cancer progress. CGI learns directly from data from previous patients, thus it uses what is called machine learning algorithms. CGI was developed as a research tool by scientists at the Barcelona Biomedical Genomics lab at IRB Barcelona. Now through CGI-Clinics, those scientists together with 17 other European institutions aim at adapting CGI into the clinics to be of use for patients.
How can patients contribute to CGI?
In the process of improving the CGI tool, we need information from thousands of tumors already sequenced, so that CGI could combine bioinformatics analysis with databases of clinical knowledge. CGI could then merge all this information and provide an interpretation of the mutations that will help clinicians to choose the best treatment for each patient. 
In consequence, our goal is to nourish the CGI platform with genomic data of cancer patients, and the first step would be to encourage patients to share their sequencing data. Would you help us? 
Why are we asking you to participate in this focus group?
Sequencing data is both complex information and useful to manage cancer treatment and progression. In CGI-Clinics we are well aware of this and would like to help patients cope with the new concepts arising in personalised cancer medicine: next generation sequencing, tumor profiling, machine-learning, variants of unknown significance, etc. We have a team of professionals that thanks to you will identify a set of questions that are important to empower patients and help them be active actors both in conversations with the oncologists and in data-sharing processes with scientists.


"""
r = Readability(original_text)

print("Flesch Reading Ease scores are: ", r.flesch())
print("Flesch - Kincaid scores are: ", r.flesch_kincaid())
print("Gunninc Fog scores are: ", r.gunning_fog())
print("Coleman Liau scores are: ", r.coleman_liau())
print("Dale Chall scores are: ", r.dale_chall())
print("Automated Readability Index scores are: ", r.ari())
print("Linsear Write scores are: ", r.linsear_write())
# print("SMOG scores are: ", r.smog(all_sentences=True))
print("Spache scores are: ", r.spache())


# r.flesch()
# r.gunning_fog()
# r.coleman_liau()
# r.dale_chall()
# r.ari()
# r.linsear_write()
# # r.smog()
# r.spache()
# Created by Christine Kakalou on 2/8/2023
# Project: ReadabilityScores
# Plugin from: https://github.com/textstat/textstat

import textstat
import regex as re

original_text = """"
Personalized medicine aims to find the best cancer treatment for the particular characteristics of each patient’s tumor. Nowadays, doctors can obtain a tumor sample using modern technology to sequence its DNA. This helps  to identify the specific mutations of the tumor and informs about treatment decisions. However, this is not an easy step since a tumor might contain hundreds of mutations. Nonetheless, it is key for the oncologist to know which mutations (usually few) are more likely to play a role in the tumor growth. This way, the best anti-cancer therapies that can target these genomic alterations can be identified. Mutations found during the tumor secuencing are complex.  Defining the mutations involved in tumor growth is a very challenging and time-consuming process."""


refactored_test = """"
What is personalised cancer medicine?
Personalized medicine means finding the best treatment for your cancer based on how your tumor is different. Doctors use advanced technology to study a tiny piece of your tumor's DNA. They look for specific changes called mutations. Figuring out these changes can be tricky because tumors can have many of them. But it's important for your doctor to find the ones that make your tumor grow. By understanding these changes, your doctor can find the best treatments that target them. Studying these changes is hard and takes time, but it helps find the best treatment for you.
What if there was a tool to help explain and understand these cancer mutations?
We made a tool called Cancer Genome Interpreter (CGI) to help doctors choose the best treatment for patients. CGI is a part of a project supported by the European Union. In this project, doctors, cancer researchers, and patient groups from 6 countries work together to make the CGI portal better and more helpful.
What is the CGI tool and CGI-Clinics?
CGI is a tool that helps doctors look at changes in tumors (they study small samples from the tumors) in a safe way. It finds the changes (called mutations) that make the cancer grow. CGI learns from the information of other patients, using special technology called machine learning. Scientists at the Barcelona Biomedical Genomics lab at IRB Barcelona created CGI as a research tool. Now, with CGI-Clinics, those scientists and 17 other European institutions want to make CGI useful for patients by using it in clinics.
How can patients help with CGI?
To make the CGI tool better, we need information from many tumors that were already studied. CGI will use this information along with medical knowledge to understand the mutations and find the best treatment for each patient. Our aim is to collect information from cancer patients, like their genes and the DNA data of their cancer, for the CGI platform. The first step is to ask patients to share this tumor information called sequencing data. Will you help us with this?
Why do we want you to be part of this group and share your thoughts?
Sequencing data is like a puzzle with complicated information, but it can really help with cancer treatment. In CGI-Clinics, we want to help patients understand all these new ideas in personalized cancer medicine, like next-generation sequencing and tumor profiling. We have a team of experts who want to hear from you and ask important questions. This will help patients feel more confident when talking to their doctors and sharing information with scientists.
"""


print("Flesch Reading Ease score is: ", textstat.flesch_reading_ease(refactored_test))
print("Flesch-Kincaid Grade Level score is: ", textstat.flesch_kincaid_grade(refactored_test))
print("Gunning Fog Index score is: ", textstat.gunning_fog(refactored_test))
print("SMOG Index score is: ", textstat.smog_index(refactored_test))
print("Coleman-Liau Index score is: ", textstat.coleman_liau_index(refactored_test))
print("Automated Readability Index score is: ", textstat.automated_readability_index(refactored_test))
print("Dale-Chall Readability Score score is: ", textstat.dale_chall_readability_score(refactored_test))
print("Difficult Words score is: ", textstat.difficult_words(refactored_test))
print("Linsear Write Formula score is: ", textstat.linsear_write_formula(refactored_test))
print("Gunning Fog score is: ", textstat.gunning_fog(refactored_test))
print("Text Standard score is: ", textstat.text_standard(refactored_test))
print("Gulpease Index score is: ", textstat.gulpease_index(refactored_test))
print("Osman score is: ", textstat.osman(refactored_test))

dummy_final_text = refactored_test.replace("tumor", "apple")

difficultWords = ['mutations', 'sequencing', 'cancer', 'tumor', 'tumors', 'treatment', 'mutation', 'mutations', 'Sequencing', 'Genomics', 'Clinics', 'clinics','CGI', 'cgi-clinics', 'scientists', 'personalized', 'personalised', 'Genome', 'genomic', 'genome', 'Interpreter', 'medical', 'clinics', 'lab', 'Lab', 'sequencing', 'researchers']
big_regex = re.compile('|'.join(map(re.escape, difficultWords)))
the_message = big_regex.sub("apple",  refactored_test)
print(the_message)

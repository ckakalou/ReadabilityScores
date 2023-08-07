# Created by Christine Kakalou on 2/8/2023
# Project: ReadabilityScores
# Plugin from https://py-readability-metrics.readthedocs.io/en/latest/


from readability import Readability

original_text = """"

Personalized medicine is an approach to find the most effective cancer treatment tailored specifically to your tumor's unique characteristics. Nowadays, doctors use advanced technology to collect a small sample of your tumor and examine its DNA through a process called sequencing. This helps identify specific mutations within the tumor, which are changes in its genetic makeup. Though this step can be complicated because tumors may have many mutations, it's crucial for your oncologist to determine which mutations are most likely driving the tumor's growth. By understanding these key mutations, your doctor can identify the best anti-cancer therapies that target these specific genetic changes. The process of analyzing mutations is challenging and takes time, but it's essential to find the most suitable treatment for you

"""

refactored_test = """"
Personalized medicine means finding the best treatment for your cancer based on how your tumor is different. Doctors use advanced technology to study a tiny piece of your tumor's DNA. They look for specific changes called mutations. Figuring out these changes can be tricky because tumors can have many of them. But it's important for your doctor to find the ones that make your tumor grow. By understanding these changes, your doctor can find the best treatments that target them. Studying these changes is hard and takes time, but it helps find the best treatment for you.
"""
r = Readability(refactored_test)

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
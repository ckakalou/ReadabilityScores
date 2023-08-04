# Created by Christine Kakalou on 2/8/2023
# Project: ReadabilityScores
#
import nltk
import random
import string

# nltk.download('all')


def get_sentence_count_and_syllables(text):
    """
    Calculates the number of sentences and syllables in the given text.

    Parameters:
        text (str): The input text.

    Returns:
        (int, int): A tuple containing the number of sentences and the number of syllables.
    """
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)

    # Count the number of syllables in the text
    syllable_count = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in words:
            word = word.lower().strip(string.punctuation)
            if word.isalpha():
                syllable_count += nltk.corpus.cmudict.dict().get(word, [0])[0][0]

    return num_sentences, syllable_count

def fry_readability_graph(samples):
    """
    Calculates and plots the Fry Readability Graph based on the provided samples.

    Parameters:
        samples (list): A list of three 100-word passages (strings).

    Returns:
        None
    """
    num_sentences_total = 0
    num_syllables_total = 0

    print("Sample\tNumber of Sentences\tNumber of Syllables")
    print("-" * 49)

    for idx, sample in enumerate(samples, start=1):
        num_sentences, num_syllables = get_sentence_count_and_syllables(sample)

        num_sentences_total += num_sentences
        num_syllables_total += num_syllables

        print(f"Sample {idx}\t\t{num_sentences}\t\t\t{num_syllables}")

    average_sentence_length = num_sentences_total / 3
    average_syllables = num_syllables_total / 3

    print(f"\nTotal\t\t\t{num_sentences_total}\t\t\t{num_syllables_total}")
    print(f"Average\t\t\t{average_sentence_length:.1f}\t\t\t{average_syllables:.1f}")

    # Plot the Fry Readability Graph
    plt.plot(average_sentence_length, average_syllables, 'ro', label='Intersection Point')
    plt.xlabel('Average Sentence Length')
    plt.ylabel('Number of Syllables')
    plt.title('Fry Readability Graph')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage:
    sample1 = "Enter your first 100-word sample here."
    sample2 = "This is the second 100-word sample. You can replace this with your own text."
    sample3 = "And here's the third 100-word sample for the demonstration."

    samples = [sample1, sample2, sample3]
    fry_readability_graph(samples)


import random

#basic features
word_list = []
iob_list = []
line_list = []
sentence_list = []
#<lemma, pos>
lemma_pos_list = []
lemma_pos_line_list = []
lemma_pos_sentence_list = []
#<word, lemma, pos>
word_lemma_pos_list = []
word_lemma_pos_line_list = []
word_lemma_pos_sentece_list = []
#<word, lemma>
word_lemma_list = []
word_lemma_line_list = []
word_lemma_sentence_list = []
#<word, pos>
word_pos_list = []
word_pos_line_list = []
word_pos_sentence_list = []

with open("../data/NLSPARQL.train.data", "r") as training_data, open("../data/NLSPARQL.train.feats.txt") as training_features:
    for x, y in zip(training_data, training_features):
        # data_tokens in form < word , IOB >
        data_tokens = x.strip().split()
        # feature_tokens in form < word , POS , lemma >
        feature_tokens = y.strip().split()
        # prefix and suffix extraction (based on user's parameter)
        if len(data_tokens) > 0 and len(feature_tokens) > 0:
            word_list.append(data_tokens[0])
            iob_list.append(data_tokens[1])
            line_list.append((data_tokens[0],data_tokens[1]))
            lemma_pos_list.append((feature_tokens[2], feature_tokens[1]))
            lemma_pos_line_list.append((feature_tokens[2], feature_tokens[1], data_tokens[1]))
            word_lemma_pos_list.append((data_tokens[0],feature_tokens[2],feature_tokens[1]))
            word_lemma_pos_line_list.append((data_tokens[0],feature_tokens[2],feature_tokens[1],data_tokens[1]))
            word_lemma_list.append((data_tokens[0], feature_tokens[2]))
            word_lemma_line_list.append((data_tokens[0], feature_tokens[2], data_tokens[1]))
            word_pos_list.append((data_tokens[0], feature_tokens[1]))
            word_pos_line_list.append((data_tokens[0], feature_tokens[1], data_tokens[1]))
        else:
            if len(line_list) > 0:
                sentence_list.append(line_list)
                line_list = []
            if len(lemma_pos_line_list) > 0:
                lemma_pos_sentence_list.append(lemma_pos_line_list)
                lemma_pos_line_list = []
            if len(word_lemma_pos_line_list) > 0:
                word_lemma_pos_sentece_list.append(word_lemma_pos_line_list)
                word_lemma_pos_line_list = []
            if len(word_lemma_line_list) > 0:
                word_lemma_sentence_list.append(word_lemma_line_list)
                word_lemma_line_list = []
            if len(word_pos_line_list) > 0:
                word_pos_sentence_list.append(word_pos_line_list)
                word_pos_line_list = []
# consider the IOB tags in the test set
test_lemma_pos_line = []
test_lemma_pos_set = []
test_word_lemma_pos_line = []
test_word_lemma_pos_set = []
test_word_lemma_line = []
test_word_lemma_set = []
test_word_pos_line = []
test_word_pos_set = []

with open("../data/NLSPARQL.test.data", "r") as test_data, open("../data/NLSPARQL.test.feats.txt") as test_features:
    for x, y in zip(test_data, test_features):
        # data_tokens in form < word , IOB >
        data_tokens = x.strip().split()
        # feature_tokens in form < word , POS , lemma >
        feature_tokens = y.strip().split()
        # prefix and suffix extraction (based on user's parameter)
        if len(data_tokens) > 0 and len(feature_tokens) > 0:
            iob_list.append(data_tokens[1])
            test_lemma_pos_line.append((feature_tokens[2],feature_tokens[1],data_tokens[1]))
            test_word_lemma_pos_line.append((data_tokens[0],feature_tokens[2],feature_tokens[1],data_tokens[1]))
            test_word_lemma_line.append((data_tokens[0],feature_tokens[2],data_tokens[1]))
            test_word_pos_line.append((data_tokens[0], feature_tokens[1], data_tokens[1]))
        else:
            if len(test_lemma_pos_line) > 0:
                test_lemma_pos_set.append(test_lemma_pos_line)
                test_lemma_pos_line = []
            if len(test_word_lemma_pos_line) > 0:
                test_word_lemma_pos_set.append(test_word_lemma_pos_line)
                test_word_lemma_pos_line = []
            if len(test_word_lemma_line) > 0:
                test_word_lemma_set.append(test_word_lemma_line)
                test_word_lemma_line = []
            if len(test_word_pos_line) > 0:
                test_word_pos_set.append(test_word_pos_line)
                test_word_pos_line = []

# LEXICON
# delete duplicates. In line_list and sentence_list there are no duplicates
unique_word_list = list(set(word_list))
unique_iob_list = list(set(iob_list))
unique_lemma_pos_list = list(set(lemma_pos_list))
unique_word_lemma_pos_list = list(set(word_lemma_pos_list))
unique_word_lemma_list = list(set(word_lemma_list))
unique_word_pos_list = list(set(word_pos_list))

with open("../data/unique_word_lexicon", "w") as word_lexicon:
    counter = 0
    for element in unique_word_list:
        word_lexicon.write(element + " " + str(counter) + "\n")
        counter += 1
    # consider UNK
    word_lexicon.write("<UNK> " + str(counter) + "\n" )
with open("../data/unique_iob_lexicon", "w") as iob_lexicon:
    counter = 0
    for element in unique_iob_list:
        iob_lexicon.write(element + " " + str(counter) + "\n")
        counter += 1
with open("../data/unique_lemma_pos_lexicon", "w") as lemma_pos_lexicon:
    counter = 0
    for element in unique_lemma_pos_list:
        # separated by '_' so that can eventually be split
        lemma_pos_lexicon.write(element[0] + "_" + element[1] + " " + str(counter) + "\n")
        counter += 1
    lemma_pos_lexicon.write("<UNK> " + str(counter) + "\n")
with open("../data/unique_word_lemma_pos_lexicon", "w") as word_lemma_pos_lexicon:
    counter = 0
    for element in unique_word_lemma_pos_list:
        # separated by '_' so that can eventually be split
        word_lemma_pos_lexicon.write(element[0] + "_" + element[1] + "_" + element[2] + " " + str(counter) + "\n")
        counter += 1
    word_lemma_pos_lexicon.write("<UNK> " + str(counter) + "\n")
with open("../data/unique_word_lemma_lexicon", "w") as word_lemma_lexicon:
    counter = 0
    for element in unique_word_lemma_list:
        # separated by '_' so that can eventually be split
        word_lemma_lexicon.write(element[0] + "_" + element[1] + " " + str(counter) + "\n")
        counter += 1
    word_lemma_lexicon.write("<UNK> " + str(counter) + "\n")
with open("../data/unique_word_pos_lexicon", "w") as word_pos_lexicon:
    counter = 0
    for element in unique_word_pos_list:
        # separated by '_' so that can eventually be split
        word_pos_lexicon.write(element[0] + "_" + element[1] + " " + str(counter) + "\n")
        counter += 1
    word_pos_lexicon.write("<UNK> " + str(counter) + "\n")
# TRAINING, TEST, VALIDATION SETS
# 30% of the sentences set will be used for the validation and the rest for the training
# Please, in case of doubt on why I am creating a validation set, visit
# http://disi.unitn.it/~passerini/teaching/2017-2018/MachineLearning/slides/19_evaluation/talk.pdf

random.shuffle(sentence_list)
random.shuffle(lemma_pos_sentence_list)
random.shuffle(word_lemma_sentence_list)
random.shuffle(word_pos_sentence_list)

training_set = sentence_list[:int(len(sentence_list) * 0.30)]
validation_set = sentence_list[int(len(sentence_list) * 0.30):]

training_lemma_pos_set = lemma_pos_sentence_list[:int(len(lemma_pos_sentence_list)*0.30)]
validation_lemma_pos_set = lemma_pos_sentence_list[int(len(lemma_pos_sentence_list)*0.30):]

training_word_lemma_pos_set = word_lemma_pos_sentece_list[:int(len(word_lemma_pos_sentece_list)*0.30)]
validation_word_lemma_pos_set = word_lemma_pos_sentece_list[int(len(word_lemma_pos_sentece_list)*0.30):]

training_word_lemma_set = word_lemma_sentence_list[:int(len(word_lemma_sentence_list)*0.30)]
validation_word_lemma_set = word_lemma_sentence_list[int(len(word_lemma_sentence_list)*0.30):]

training_word_pos_set = word_pos_sentence_list[:int(len(word_pos_sentence_list)*0.30)]
validation_word_pos_set = word_pos_sentence_list[int(len(word_pos_sentence_list)*0.30):]

# save the training and the validation set in a file
with open("../data/training_set", "w") as training_set_file:
    for list in training_set:
        for element in list:
            training_set_file.write(str(element[0]) + " " + str(element[1]) + "\n")
        training_set_file.write("\n")
with open("../data/validation_set", "w") as validation_set_file:
    for list in validation_set:
        for element in list:
            validation_set_file.write(str(element[0]) + " " + str(element[1]) + "\n")
        validation_set_file.write("\n")

# save the training, the test and the validation set in a file (<lemma,pos>)
with open("../data/training_lemma_pos_set", "w") as training_lemma_pos_set_file:
    for list in training_lemma_pos_set:
        for element in list:
            training_lemma_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        training_lemma_pos_set_file.write("\n")
with open("../data/validation_lemma_pos_set", "w") as validation_lemma_pos_set_file:
    for list in validation_lemma_pos_set:
        for element in list:
            validation_lemma_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        validation_lemma_pos_set_file.write("\n")
with open("../data/test_lemma_pos_set", "w") as test_lemma_pos_set_file:
    for list in test_lemma_pos_set:
        for element in list:
            test_lemma_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        test_lemma_pos_set_file.write("\n")

# save the training, the test and the validation set in a file (<word,lemma,pos>)
with open("../data/training_word_lemma_pos_set", "w") as training_word_lemma_pos_set_file:
    for list in training_word_lemma_pos_set:
        for element in list:
            training_word_lemma_pos_set_file.write(element[0] + "_" + element[1] + "_" + element[2] + " " + element[3] + "\n")
        training_word_lemma_pos_set_file.write("\n")
with open("../data/validation_word_lemma_pos_set", "w") as validation_word_lemma_pos_set_file:
    for list in validation_word_lemma_pos_set:
        for element in list:
            validation_word_lemma_pos_set_file.write(element[0] + "_" + element[1] + "_" + element[2] + " " + element[3] + "\n")
        validation_word_lemma_pos_set_file.write("\n")
with open("../data/test_word_lemma_pos_set", "w") as test_word_lemma_pos_set_file:
    for list in test_word_lemma_pos_set:
        for element in list:
            test_word_lemma_pos_set_file.write(element[0] + "_" + element[1] + "_" + element[2] + " " + element[3] + "\n")
        test_word_lemma_pos_set_file.write("\n")

# save the training, the test and the validation set in a file (<word,lemma>)
with open("../data/training_word_lemma_set", "w") as training_word_lemma_set_file:
    for list in training_word_lemma_set:
        for element in list:
            training_word_lemma_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        training_word_lemma_set_file.write("\n")
with open("../data/validation_word_lemma_set", "w") as validation_word_lemma_set_file:
    for list in validation_word_lemma_set:
        for element in list:
            validation_word_lemma_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        validation_word_lemma_set_file.write("\n")
with open("../data/test_word_lemma_set", "w") as test_word_lemma_set_file:
    for list in test_word_lemma_set:
        for element in list:
            test_word_lemma_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        test_word_lemma_set_file.write("\n")

# save the training, the test and the validation set in a file (<word,pos>)
with open("../data/training_word_pos_set", "w") as training_word_pos_set_file:
    for list in training_word_pos_set:
        for element in list:
            training_word_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        training_word_pos_set_file.write("\n")
with open("../data/validation_word_pos_set", "w") as validation_word_pos_set_file:
    for list in validation_word_pos_set:
        for element in list:
            validation_word_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        validation_word_pos_set_file.write("\n")
with open("../data/test_word_pos_set", "w") as test_word_pos_set_file:
    for list in test_word_pos_set:
        for element in list:
            test_word_pos_set_file.write(element[0] + "_" + element[1] + " " + element[2] + "\n")
        test_word_pos_set_file.write("\n")

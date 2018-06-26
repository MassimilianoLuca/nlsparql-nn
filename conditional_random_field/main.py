import sys
import os

if len(sys.argv) < 2:
    print('Please, use --help and look at the helper')
    exit(0)

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print('USAGE:')
    print('Parameter 1: the index to split prefixes and suffixes. It must be a positive integer number (i.e., 3)')
    print('Parameter 2: the template for the crf. The templates can be found in the folder \"template\". Please to know which one you should choose, open them and read the description.')
    print('Parameter 3: the name of the file in which the results are going to be stored. If the file exists, it will be overwritted otherwise it will be created. The file should be saved in \"result\"')
    print('Parameter 4: the name of the file in which the evaluations are going to be stored. If the file exists, it will be overwritted otherwise it will be created. The file should be saved in \"evaluation\"')
    print('Parameter 5: the name of the file in which the model is going to be stored. If the file exists, it will be overwritted otherwise it will be created. The file should be saved in \"model\"')
    print()
    print('Example:')
    print('python main.py 3 template/base result/base_result evaluation/base_evaluation model/base_model')
    exit(0)

# gathering info from the training files
with open("data/NLSPARQL.train.data", "r") as training_data, open("data/NLSPARQL.train.feats.txt", "r") as training_features, open("data/training.data", "w") as training_writer:
    for x, y in zip(training_data, training_features):
        # data_tokens in form < word , IOB >
        data_tokens = x.strip().split()
        # feature_tokens in form < word , POS , lemma >
        feature_tokens = y.strip().split()
        # prefix and suffix extraction (based on user's parameter)
        if len(data_tokens) > 0 and len(feature_tokens) > 0:
            if len(data_tokens[0]) > int(sys.argv[1]):
                prefix = data_tokens[0][0:int(sys.argv[1])]
                suffix = data_tokens[0][-int(sys.argv[1]):]
            else:
                # where NPS = no prefix and suffix
                prefix = "NPS"
                suffix = "NPS"
            training_writer.write(data_tokens[0] + " " + feature_tokens[2] + " " + feature_tokens[1] + " " + prefix + " " + suffix + " " + data_tokens[1] + "\n")
        else:
            training_writer.write("\n")

# gathering info from the test file
with open("data/NLSPARQL.test.data", "r") as test_data, open("data/NLSPARQL.test.feats.txt", "r") as test_features, open("data/test.data", "w") as test_writer:
    for x, y in zip(test_data, test_features):
        # data_tokens in form < word , IOB >
        data_tokens = x.strip().split()
        # feature_tokens in form < word , POS , lemma >
        feature_tokens = y.strip().split()
        # prefix and suffix extraction (based on user's parameter)
        if len(data_tokens) > 0 and len(feature_tokens) > 0:
            if len(data_tokens[0]) > int(sys.argv[1]):
                prefix = data_tokens[0][0:int(sys.argv[1])]
                suffix = data_tokens[0][-int(sys.argv[1]):]
            else:
                # where NPS = no prefix and suffix
                prefix = "NPS"
                suffix = "NPS"
            test_writer.write(data_tokens[0] + " " + feature_tokens[2] + " " + feature_tokens[1] + " " + prefix + " " + suffix + " " + data_tokens[1] + "\n")
        else:
            test_writer.write("\n")

os.system('crf_learn ' + str(sys.argv[2]) +' data/training.data '+ str(sys.argv[5]))
os.system('crf_test -m' + str(sys.argv[5]) +' data/test.data > '+ str(sys.argv[3]))
os.system(' perl evaluation/conlleval.pl -d \'\s\' < ' + str(sys.argv[3]) + ' > ' + str(sys.argv[4]) )

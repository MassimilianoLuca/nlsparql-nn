# (Update) Exam evaluation

This project and (https://github.com/MassimilianoLuca/nlsparql-wfst)[this] are part of the Language Understanding System class that I took in my Master Degree at the University of Trento. 

Mark (ITA): 30/30
Mark (US): A


# CRF

Under the conditional_random_field folder, the CRF model can be found. To generate the results, elaborate the training and test sets and to create the other necessary files, you just have to use the main.py script. You can run it using Python 3 by typing python3 main.py or python main.py (depending on the environment of your machine).


By typing python main.py -h or python main.py --help, a small usage guideline appears in your terminal. Here is an example on how to run it:

python main.py 3 template/win3 result/win3_result evaluation/win3_evaluation model/win3_model

__Important note:__ the only file that __must__ exists is the template file. All the others are generated.

# Elman RNN

__NOTE: Python < 3, Theano and an evironment variable to rnn_slu folder are needed to run this part.__

First, go in recursive_neural_network_elman/support and run generator.py. This script will generate all the necessary files in the folder data. Once you did it,


__NOTE: the following scripts must be run from the upper level folder (nlsparql-nn). If you run it from other folders, an error like this should appears__
python: can't open file 'rnn_slu/lus/rnn_elman_train.py': [Errno 2] No such file or directory

Example of training:

python rnn_slu/lus/rnn_elman_train.py recursive_neural_network_elman/data/training_word_pos_set recursive_neural_network_elman/data/validation_word_pos_set recursive_neural_network_elman/data/unique_word_pos_lexicon recursive_neural_network_elman/data/unique_iob_lexicon recursive_neural_network_elman/rnn_models/config3.cfg recursive_neural_network_elman/results/config3_word_pos_elman

Example of test:

python rnn_slu/lus/rnn_elman_test.py config3_word_pos_elman recursive_neural_network_elman/data/test_word_pos_set recursive_neural_network_elman/data/unique_word_pos_lexicon recursive_neural_network_elman/data/unique_iob_lexicon recursive_neural_network_elman/rnn_models/config3.cfg out_config3_word_pos_elman

# Jordan RNN

__NOTE: Python < 3, Theano and an evironment variable to rnn_slu folder are needed to run this part.__

First, go in recursive_neural_network_jordan/support and run generator.py. This script will generate all the necessary files in the folder data. Once you did it,


__NOTE: the following scripts must be run from the upper level folder (nlsparql-nn). If you run it from other folders, an error like this should appears__
python: can't open file 'rnn_slu/lus/rnn_jordan_train.py': [Errno 2] No such file or directory

Example of training:

python rnn_slu/lus/rnn_jordan_train.py recursive_neural_network_jordan/data/training_word_pos_set recursive_neural_network_jordan/data/validation_word_pos_set recursive_neural_network_jordan/data/unique_word_pos_lexicon recursive_neural_network_jordan/data/unique_iob_lexicon recursive_neural_network_jordan/rnn_models/config3.cfg recursive_neural_network_jordan/results/config3_word_pos_jordan

Example of test:

python rnn_slu/lus/rnn_jordan_test.py config3_word_pos_jordan recursive_neural_network_jordan/data/test_word_pos_set recursive_neural_network_jordan/data/unique_word_pos_lexicon recursive_neural_network_jordan/data/unique_iob_lexicon recursive_neural_network_jordan/rnn_models/config3.cfg out_config3_word_pos_jordan

# RNN_SLU

In this folder a set of scripts to train and test Jordan RNNs and Elman RNNs can be found. All the scripts in this folder have been provided during the classes. __I did not work on this code__.

#!/usr/bin/python
import tensorflow as tf

from .config import Config
from .model import CaptionGenerator
from .dataset import prepare_train_data, prepare_eval_data, prepare_test_data

FLAGS = tf.app.flags.FLAGS

tf.flags.DEFINE_string('phase', 'test',
                       'The phase can be train, eval or test')

tf.flags.DEFINE_boolean('load', False,
                        'Turn on to load a pretrained model from either \
                        the latest checkpoint or a specified file')

tf.flags.DEFINE_string('model_file', '/home/ubuntu/s03p23d107/backend/AI/captioning/models/289999.npy',
                       'If sepcified, load a pretrained model from this file')

tf.flags.DEFINE_boolean('load_cnn', False,
                        'Turn on to load a pretrained CNN model')

tf.flags.DEFINE_string('cnn_model_file', './vgg16_no_fc.npy',
                       'The file containing a pretrained CNN model')

tf.flags.DEFINE_boolean('train_cnn', False,
                        'Turn on to train both CNN and RNN. \
                         Otherwise, only RNN is trained')

tf.flags.DEFINE_integer('beam_size', 3,
                        'The size of beam search for caption generation')

def main(argv):
    config = Config()
    config.phase = FLAGS.phase
    config.train_cnn = FLAGS.train_cnn
    config.beam_size = FLAGS.beam_size

    with tf.Session() as sess:
        # testing phase
        data, vocabulary = prepare_test_data(config)
        model = CaptionGenerator(config)
        model.load(sess, FLAGS.model_file)
        tf.get_default_graph().finalize()
        text = model.test(sess, data, vocabulary, argv)
    # print(text)
    return text

if __name__ == '__main__':
    tf.app.run()
